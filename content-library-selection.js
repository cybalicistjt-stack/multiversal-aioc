(()=>{
  'use strict';

  let activating = false;

  function cardFromEvent(event) {
    return event.target?.closest?.('#objectList .object-card[data-id]') || null;
  }

  function openWorkbench() {
    const explorer = document.querySelector('[data-mode="explorer"]');
    if (!explorer?.classList.contains('active')) return;
    const workbench = document.querySelector('[data-mode="workbench"]');
    if (workbench && !workbench.disabled) workbench.click();
  }

  function clearActiveCards() {
    const activeCards = document.querySelectorAll?.('#objectList .object-card.active') || [];
    activeCards.forEach(item => item.classList.remove('active'));
  }

  function activateCard(card, invokeCoreClick) {
    if (!card || activating) return;
    activating = true;
    try {
      clearActiveCards();
      card.classList.add('active');
      if (invokeCoreClick) card.click();
      queueMicrotask(openWorkbench);
    } finally {
      queueMicrotask(() => { activating = false; });
    }
  }

  function handleClick(event) {
    const card = cardFromEvent(event);
    if (!card || activating) return;
    activateCard(card, false);
  }

  function handlePointerUp(event) {
    const card = cardFromEvent(event);
    if (!card) return;
    if (event.pointerType && event.pointerType !== 'touch' && event.pointerType !== 'pen') return;
    event.preventDefault?.();
    activateCard(card, true);
  }

  function handleTouchEnd(event) {
    const card = cardFromEvent(event);
    if (!card) return;
    event.preventDefault?.();
    activateCard(card, true);
  }

  const openSelectedObject = handleClick;

  document.addEventListener('click', handleClick);
  document.addEventListener('pointerup', handlePointerUp, { passive: false });
  document.addEventListener('touchend', handleTouchEnd, { passive: false });

  window.ContentLibrarySelectionController = Object.freeze({
    openSelectedObject,
    activateCard,
    handleClick,
    handlePointerUp,
    handleTouchEnd
  });
})();
