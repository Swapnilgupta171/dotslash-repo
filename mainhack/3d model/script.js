let car; // Car object
let friction = 0.01; // Default friction
let accelerationValue = 1; // Default acceleration
let isMoving = false; // Track if the car is in motion

function setup() {
  createCanvas(windowWidth, windowHeight);

  // Create the car object
  car = {
    x: width / 4,
    y: height / 2,
    width: 120,
    height: 60,
    wheelRadius: 20,
    velocity: 0,
    acceleration: 0,
    color: color(255, 0, 0),
  };

  // Setup sliders
  const frictionSlider = document.getElementById("friction-slider");
  const accelerationSlider = document.getElementById("acceleration-slider");
  frictionSlider.addEventListener("input", () => {
    friction = parseFloat(frictionSlider.value);
    document.getElementById("friction-value").innerText = friction.toFixed(2);
  });
  accelerationSlider.addEventListener("input", () => {
    accelerationValue = parseFloat(accelerationSlider.value);
    document.getElementById("acceleration-value").innerText = accelerationValue.toFixed(1);
  });
}

function draw() {
  background(230);

  // Draw road
  fill(100);
  rect(0, car.y + car.height / 2, width, car.height + 40);

  // Draw the car body
  fill(car.color);
  rect(car.x, car.y, car.width, car.height, 10);

  // Draw car wheels
  fill(50);
  ellipse(car.x + 20, car.y + car.height, car.wheelRadius * 2); // Front wheel
  ellipse(car.x + car.width - 20, car.y + car.height, car.wheelRadius * 2); // Rear wheel

  // Display velocity
  fill(50);
  textSize(16);
  textAlign(LEFT);
  text(`Velocity: ${car.velocity.toFixed(2)} m/s`, 20, height - 20);

  // Update car's position if in motion
  if (isMoving) {
    car.velocity += car.acceleration; // Update velocity
    car.x += car.velocity; // Update position

    // Apply friction
    if (car.velocity > 0) {
      car.velocity -= friction;
    } else {
      car.velocity = 0; // Stop the car completely
      isMoving = false;
    }
  }

  // Prevent car from going out of bounds
  if (car.x + car.width > width || car.x < 0) {
    car.velocity = 0;
    isMoving = false;
  }
}

function keyPressed() {
  if (keyCode === RIGHT_ARROW) {
    // Move forward
    car.acceleration = accelerationValue;
    isMoving = true;
  } else if (keyCode === UP_ARROW) {
    // Increase acceleration
    car.acceleration = accelerationValue;
    car.velocity += car.acceleration;
  } else if (keyCode === DOWN_ARROW) {
    // Apply brakes
    car.acceleration = -accelerationValue / 2; // Decelerate
    car.velocity += car.acceleration;
  }
}
