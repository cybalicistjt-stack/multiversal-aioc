(()=>{'use strict';
const detail=()=>document.querySelector('#detail');
function focusDetail(){
  const panel=detail();
  if(!panel)return;
  panel.setAttribute('tabindex','-1');
  panel.scrollIntoView({behavior:'smooth',block:'start'});
  setTimeout(()=>panel.focus({preventScroll:true}),350);
  if(!document.querySelector('#backToAssistantQueue')){
    const button=document.createElement('button');
    button.id='backToAssistantQueue';
    button.type='button';
    button.textContent='← Back to object queue';
    button.style.cssText='display:none;margin:0 0 12px;padding:10px 12px;border:1px solid #7c3488;border-radius:9px;background:#25102c;color:white;font-weight:700';
    button.addEventListener('click',()=>document.querySelector('#queueList')?.scrollIntoView({behavior:'smooth',block:'start'}));
    panel.prepend(button);
  }
  const back=document.querySelector('#backToAssistantQueue');
  if(back)back.style.display=matchMedia('(max-width:800px)').matches?'inline-block':'none';
}
document.addEventListener('click',event=>{
  if(!event.target.closest('.queue-item[data-id]'))return;
  setTimeout(focusDetail,0);
},true);
})();
