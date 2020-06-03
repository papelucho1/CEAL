
requestAnimationFrame(() => {
    const boxes = document.querySelectorAll(".box");
  
    function getIntersectionRatio(i) {
      const a = [window.scrollY, window.scrollY + window.innerHeight];
      const b = [boxes[i].offsetTop, boxes[i].offsetTop + boxes[i].clientHeight];
  
      const max = Math.max(a[0], b[0]);
      const min = Math.min(a[1], b[1]);
  
      return Math.max(0, (min - max) / (b[1] - b[0]));
    }
  
    function onScroll() {
      const boxes = document.querySelectorAll(".box");
      for (let i = 0; i < boxes.length; i += 1) {
        const intersection = getIntersectionRatio(i);
        const top = boxes[i].offsetTop - window.pageYOffset < 0;
        boxes[i].firstChild.style.cssText = `
          transform-origin: ${top ? "center center" : "top center"};
          position: ${top ? "fixed" : "absolute"};
          transform: scale(${intersection});
          opacity: ${intersection};
        `;
      }
      requestAnimationFrame(onScroll);
    }
  
    onScroll();
  });