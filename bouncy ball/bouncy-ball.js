const selectorElement = document.getElementById('selector');
      const maxSpeed = 0.15;
      const friction = 0.003;
      let lastTime;
      let speed = { x: 0, y: 0 };
      let position = { x: 50, y: 50 };

      function start() {
        lastTime = Date.now();
        timeout = setInterval(loop, 17);
        speed = { x: Math.random() - 0.5, y: Math.random() - 0.5 };
      }

      function loop() {
        var thisTime = Date.now();
        var deltaTime = thisTime - lastTime;

        position = {
          x: position.x + speed.x * deltaTime * maxSpeed,
          y: position.y + speed.y * deltaTime * maxSpeed,
        };

        speed = {
          x: speed.x * (1 - friction),
          y: speed.y * (1 - friction),
        };

        if (Math.abs(speed.x) <= 2 * friction * maxSpeed) {
          speed.x = 0;
        }

        if (Math.abs(speed.y) <= 2 * friction * maxSpeed) {
          speed.y = 0;
        }

        if (position.x >= 100 || position.x <= 0) {
          speed.x = -speed.x * 1.0011;
        }

        if (position.y >= 100 || position.y <= 0) {
          speed.y = -speed.y * 1.0011;
        }

        selectorElement.style.top = position.y + "%"
        selectorElement.style.left = position.x + "%"

        lastTime = thisTime;
      }