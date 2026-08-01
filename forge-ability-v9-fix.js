(() => {
  const install = () => {
    if (!window.AbilityForge9 || window.AbilityForge9.__closeFix) return;
    const original = window.AbilityForge9.saveFinal.bind(window.AbilityForge9);
    window.AbilityForge9.saveFinal = (...args) => {
      const result = original(...args);
      setTimeout(() => {
        document.querySelector('#ab9')?.remove();
        document.body.style.overflow = '';
        if (typeof window.render === 'function') window.render();
      }, 0);
      return result;
    };
    window.AbilityForge9.__closeFix = true;
  };
  new MutationObserver(install).observe(document.body, {childList:true, subtree:true});
  setTimeout(install, 100);
})();