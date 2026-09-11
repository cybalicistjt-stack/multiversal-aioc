import json
import tempfile
import unittest
from pathlib import Path
from dwc_training_gate import authorize, digest
from dwc_audio_gate import decide


class Gates(unittest.TestCase):
    def fixture(self,d):
        wav=Path(d)/'reference.wav';wav.write_bytes(b'audio fixture')
        p=Path(d)/'audio.json';p.write_text(json.dumps([{'audio':wav.name,'sha256':digest(wav)}]))
        return p

    def test_failed_and_missing_human_blocks_training(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.fixture(d)
            request={'kind':'tiny_overfit','rows':12,'max_steps':200,'max_seconds':300,'corpus_sha256':'corpus'}
            target={'status':'TARGET_MACHINE_PASS','corpus_sha256':'corpus'}
            for status in ('NOT_RUN','PERCEPTUAL_SMOKE_FAIL','CATASTROPHIC_FAIL'):
                receipt={'status':status,'reviewer':'John Brandon Turner','audio_manifest_sha256':digest(p),'owner_evidence':'test'}
                self.assertFalse(authorize(request,target,receipt,p)['authorized'])

    def test_exact_receipt_and_budget(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.fixture(d)
            request={'kind':'tiny_overfit','rows':12,'max_steps':200,'max_seconds':300,'corpus_sha256':'corpus'}
            target={'status':'TARGET_MACHINE_PASS','corpus_sha256':'corpus'}
            receipt={'status':'PERCEPTUAL_SMOKE_PASS','reviewer':'John Brandon Turner','audio_manifest_sha256':digest(p),'owner_evidence':'fixture only'}
            self.assertTrue(authorize(request,target,receipt,p)['authorized'])
            self.assertFalse(authorize({**request,'max_steps':201},target,receipt,p)['authorized'])
            (Path(d)/'reference.wav').write_bytes(b'changed audio')
            self.assertFalse(authorize(request,target,receipt,p)['authorized'])
            p.write_text('[1]')
            self.assertFalse(authorize(request,target,receipt,p)['authorized'])

    def test_machine_only_tranche_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.fixture(d)
            receipt={'status':'PERCEPTUAL_SMOKE_PASS','reviewer':'John Brandon Turner','audio_manifest_sha256':digest(p),'owner_evidence':'fixture only'}
            req={'kind':'small_tranche','max_steps':100,'max_seconds':100,'corpus_sha256':'c'}
            self.assertFalse(authorize(req,{'status':'TARGET_MACHINE_PASS','corpus_sha256':'c'},receipt,p)['authorized'])

    def test_calibration_rejects_collapse_and_incomplete_overfit(self):
        good={'own_target_top1_fraction':1.,'own_target_margin':6.,'contrast_ratio_min':1.}
        bad={'own_target_top1_fraction':.083,'own_target_margin':-7.,'contrast_ratio_min':.003}
        self.assertEqual(decide(good,bad,bad)['status'],'OUTPUT_MACHINE_FAIL')
        self.assertEqual(decide(good,bad,good)['status'],'OUTPUT_MACHINE_PASS')
        self.assertEqual(decide(good,bad,{**good,'own_target_top1_fraction':.9})['status'],'OUTPUT_MACHINE_FAIL')
        self.assertEqual(decide(good,good,good)['status'],'UNCALIBRATED_BLOCK')


if __name__=='__main__':unittest.main()
