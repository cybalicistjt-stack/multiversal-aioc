(()=>{
  'use strict';

  function openSelectedObject(event) {
    const card = event.target.closest?.('#objectList .object-card[data-id]');
    if (!card) return;

    const explorer = document.querySelector('[data-mode="explorer"]');
    if (!explorer?.classList.contains('active')) return;

    queueMicrotask(() => {
      const workbench = document.querySelector('[data-mode="workbench"]');
      if (workbench && !workbench.disabled) workbench.click();
    });
  }

  document.addEventListener('click', openSelectedObject);

  window.ContentLibrarySelectionController = Object.freeze({
    openSelectedObject
  });
})();
