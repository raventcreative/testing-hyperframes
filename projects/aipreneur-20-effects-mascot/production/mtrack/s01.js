vt.set(V, {"fx": 540, "fy": 1800, "h": 1470, "yaw": 0, "pitch": 5}, 4);
vt.fromTo(V, {"fx": 540, "fy": 1800, "h": 1470, "yaw": 0, "pitch": 5}, {"fx": 540, "fy": 1800, "h": 1470, "yaw": -4, "pitch": 5, "duration": 1.52, "ease": "sine.inOut", "immediateRender": false}, 4);
vt.fromTo(V, {"fx": 540, "fy": 1800, "h": 1470, "yaw": -4, "pitch": 5}, {"fx": 540, "fy": 1800, "h": 1470, "yaw": 0, "pitch": 5, "duration": 0.713, "ease": "sine.inOut", "immediateRender": false}, 5.52);
vt.set("#m-clip", {"clipPath": "inset(300px 90px 440px 90px round 36px)"}, 4);
vt.fromTo("#m-clip", {"clipPath": "inset(300px 90px 440px 90px round 36px)"}, {"clipPath": "inset(300px 90px 440px 90px round 36px)", "duration": 1.873, "ease": "none", "immediateRender": false}, 4);
vt.fromTo("#m-clip", {"clipPath": "inset(300px 90px 440px 90px round 36px)"}, {"clipPath": "inset(-400px -400px -400px -400px round 0px)", "duration": 0.36, "ease": "power2.in", "immediateRender": false}, 5.873);
