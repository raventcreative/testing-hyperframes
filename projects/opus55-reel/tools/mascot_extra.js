      const WALK = [0.0, 0.85, 2, 0.3];
      const EXTRA = (t) => M3.walk(t, WALK[0], WALK[1], WALK[2], WALK[3]).bones;
      const BOB = (t) => M3.walk(t, WALK[0], WALK[1], WALK[2], WALK[3]).bob;
