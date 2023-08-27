// Get First Table and Corresponding Button
const firstTable = document.querySelector("#table-1");
const firstButton = document.querySelector("#view-stats-1");

// Get Second Table and Corresponding Button
const secondTable = document.querySelector("#table-2");
const secondButton = document.querySelector("#view-stats-2");

// Get Third Table and Corresponding Button
const thirdTable = document.querySelector("#table-3");
const thirdButton = document.querySelector("#view-stats-3");

// Create Function for First Table - Button Pair
firstButton.addEventListener("click", () => {
  // Check if the table is minimized
  if (firstTable.style.width === "150px") {
    // Expand the table
    firstTable.style.width = "100%";

    // Hide the table caption
    firstTable.caption.style.display = "none";

    // Show the table rows
    for (const row of firstTable.querySelectorAll(".hidden")) {
      row.style.display = "table-row";
    }
  } else {
    // Minimize the table
    firstTable.style.width = "150px";

    // Show the table caption
    firstTable.caption.style.display = "table-cell";

    // Hide the table rows
    for (const row of firstTable.querySelectorAll(".hidden")) {
      row.style.display = "none";
    }
  }
});

// Create Function for Second Table - Button Pair
secondButton.addEventListener("click", () => {
  // Check if the table is minimized
  if (secondTable.style.width === "150px") {
    // Expand the table
    secondTable.style.width = "100%";

    // Hide the table caption
    secondTable.caption.style.display = "none";

    // Show the table rows
    for (const row of secondTable.querySelectorAll(".hidden")) {
      row.style.display = "table-row";
    }
  } else {
    // Minimize the table
    secondTable.style.width = "150px";

    // Show the table caption
    secondTable.caption.style.display = "table-cell";

    // Hide the table rows
    for (const row of secondTable.querySelectorAll(".hidden")) {
      row.style.display = "none";
    }
  }
});

// Create Function for Third Table - Button Pair
thirdButton.addEventListener("click", () => {
  // Check if the table is minimized
  if (thirdTable.style.width === "150px") {
    // Expand the table
    thirdTable.style.width = "100%";

    // Hide the table caption
    thirdTable.caption.style.display = "none";

    // Show the table rows
    for (const row of thirdTable.querySelectorAll(".hidden")) {
      row.style.display = "table-row";
    }
  } else {
    // Minimize the table
    thirdTable.style.width = "150px";

    // Show the table caption
    thirdTable.caption.style.display = "table-cell";

    // Hide the table rows
    for (const row of thirdTable.querySelectorAll(".hidden")) {
      row.style.display = "none";
    }
  }
});
