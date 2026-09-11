# DWC catastrophic speech failure: measured recovery audit

## Finding

The final R2C human failure is authoritative. It is corroborated by a severe loss
of phoneme identity conditioning already present at the stored R1 endpoint and
worsening through R2B. R2C then froze the damaged text encoder. Correct exact-ID
plumbing and audible waveforms never established learned pronunciation.

The verified checkpoint is c26ecb279ed5759a4c251ad54c80ebaa38e055194f6698681922b33e64269a3e,
281761455 bytes. All 125 reviewed WAVs match the persisted final machine-gate
files byte for byte. This rules out an accidental review-package rerender as the
explanation. Earlier 625/625 waveform results are preserved, not reinterpreted as
speech quality.

## Measured scope

All 799 repaired targets were measured. Twelve deliberately selected utterances
were rendered at eight checkpoints, including four exact one-phone contrast
pairs. Equal-length single-phone substitution, permutation, repeated-a and
substituted-u perturbations used the same RNG seed. A separate zero-noise control
clamped duration to eight frames per token. Text-encoder, prior mean and decoder
input tensors were compared. Four posterior reconstructions per checkpoint
tested the acoustic path while bypassing text conditioning. No training occurred.

## Conditioning collapse

For the fixed-duration one-phone change, relative encoder change falls from
0.457 at the fresh warm-start to 0.0152 at R1 and 0.00106 at R2B-256/final R2C.
Relative decoder-input change falls from 0.378 to 0.00590 at R1 and 0.000584 at
final R2C. MFCC trajectory difference falls from 9.56 to 0.224 to 0.0215.

The default-noise fixed-seed control agrees: final single-phone substitution
leaves duration exactly unchanged (1.13778 s) and yields MFCC difference 0.0561.
Even replacing all segmental phones with u produces only 0.1397 difference.
This is stronger evidence than simply observing a high spectral correlation:
phoneme content was deliberately changed while length and RNG were controlled.

Own-target nearest-neighbor retrieval on the 12-row panel is 1/12 at fresh
warm-start, 0/12 at R1, and 1/12 at final R2C. The smallest final contrast retains
only 0.00270 of its reference MFCC distance. Yet median global pair distance is
15.56: a global diversity threshold alone would miss the collapse.

The final text-only median own-target distance is 23.98. Posterior-oracle
reconstruction distances for the four tested examples are 5.10-5.72. R1 shows
the same gap. This supports a working acoustic decoder paired with a poorly
learned prior/conditioning path; it does not establish that the oracle sounds
natural, nor is oracle audio a recovered text-to-speech candidate.

## Earliest supported boundary

The fresh exact-58 warm-start was never a learned DWC speech system: the actual
Piper `_warmstart_vocoder_from_ckpt` copies only dec, enc_q and flow. The text
encoder/embedding and duration model start new. Its 1/12 retrieval is consistent
with that fact; random input sensitivity is not learned speech.

Severe conditioning suppression is directly established by the stored R1 batch128
checkpoint, before flow-restoration promotion. There are no intermediate R1
weight snapshots here to locate its onset to a specific optimizer update.
Preserved eight-row audio probes from steps 1,8,...128 remain spectrally diverse
across different lengths; they cannot by themselves date perceptual collapse.
It would be unsupported to claim a usable DWC warm-start was destroyed at an
exact early step. The earliest process error was treating technical warm-start
viability as sufficient to proceed without a tiny learned-speech demonstration.

## Why the loss/gates allowed this

Piper `models.py` forward lines 718-763 decodes posterior z from target spectra.
Text prior alignment is encouraged through KL/duration objectives, but mel and
adversarial reconstruction use posterior samples. Inference lines 784-813 instead
uses enc_p, predicted durations, sampled prior and reversed flow. Lower posterior
reconstruction loss therefore does not prove that text-only inference learned
phonemic content. The measurements demonstrate this gap in this lineage.

Restoring flow to obtain amplitude, then restoring/freezing duration and enc_p,
optimized the waveform gate while retaining weak conditioning. The R2C source
and final encoder/prior perturbation responses are exactly equal in this audit,
consistent with the recorded frozen modules. Decoder-only improvements cannot
teach a frozen collapsed encoder to distinguish the intended sounds.

An additional historical harness defect remains documented: its probe calls
`model.eval()` without restoring training mode before the next loss, and reseeds
the training RNG. Later protected scripts addressed RNG isolation, but that
does not repair learned conditioning. This audit does not assign a causal share
of collapse to that defect without a controlled experiment.

## Repaired targets

The targets are not globally identical: median MFCC pair distance is 24.27,
duration/ID-length Spearman correlation 0.936, and the four chosen segmental
contrasts have distances 6.31, 11.52, 15.63 and 25.51. This refutes a claim that
all targets are the same waveform. It does NOT prove distinguishable human speech.

There are 34 exact audio duplicate groups, 150 excess repeated rows, hence 649
unique audio byte hashes despite 799 unique filenames. Most repeats have the
same ID sequence. The one differing-ID duplicate is Nei with/without a period;
the proxy explicitly drops that punctuation distinction. This is not evidence
that an actual segmental minimal pair was merged. The complete near-neighbor
list and mapping collision are retained for review. Repeated rows also change
training weights and should be deduplicated in the tiny experiment.

eSpeak proxies are synthetic and approximate special phones. Acoustic diversity
cannot certify their native CNS realization or naturalness. No human target
approval is known. Twelve reference-only clips are prepared for that prerequisite.
The old v0.1 silent/colliding corpus remains rejected and is not reused.

## Repair and unresolved question

Legacy training is blocked at its Python entrypoints and local bootstrap launcher.
New fail-closed checks require exact-artifact human target approval, tiny own-target
retrieval, contrast retention, conditioning controls and human output smoke before
larger training. The new diagnostic gate rejects final R2C on all three metrics.
The thresholds are explicitly provisional: no natural-positive/tiny-overfit
calibration evidence exists yet, so no production authorization is granted.

No recovered candidate has passed. The smallest path is target listening first,
then a budgeted 8-16-row conditioning experiment against the original acoustic
teacher. If those references are unacceptable, obtain only the tiny replacement
CNS recording set before training. No 799-row run or engine migration is justified.

Evidence lives at `/home/antiquaria/multiversal/dwc-tts/runs/perceptual_recovery_20260910`.
JSON files contain exact selections, checkpoint hashes, tensor deltas, target
metrics, all measured contrasts, early probe metrics and reviewed-file identity.
