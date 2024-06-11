
  function createNewDiv() {
    console.log("Creating new div...")
    let pageContainer = document.getElementById('overflowTest_pageContainer');
    const newDiv = document.createElement('div');
    newDiv.className = 'e10402003 overflowTest_page';
    if (pageContainer.firstChild) {
      // Insert the new div before the first child
      pageContainer.insertBefore(newDiv, pageContainer.firstChild);
    } else {
      // If pageContainer is empty, just append the new div
      pageContainer.appendChild(newDiv);
    }
    return newDiv;
  }

  function moveContent(oldDiv, newDiv) {
    let elements = oldDiv.querySelectorAll('.overflowTest_element');
    console.log(elements)
    for (let el of elements) {
      // Move each element if there is overflow
      if (oldDiv.scrollHeight > oldDiv.clientHeight) {
        newDiv.appendChild(el);
      }
    }
    // Check if newDiv overflows and needs to be split further
    if (newDiv.scrollHeight > newDiv.clientHeight) {
      let anotherNewDiv = createNewDiv();
      moveContent(newDiv, anotherNewDiv);
    }
  }

  function checkAndMoveContent() {
    console.log("Checking for page Overflow...")
    let contentDivs = document.querySelectorAll('.overflowTest_page');
    console.log(contentDivs)
    contentDivs.forEach(div => {
      console.log(div.scrollHeight)
      console.log(div.clientHeight)
      if (div.scrollHeight > div.clientHeight) {
        console.log("Overflow...")
        let newDiv = createNewDiv();
        moveContent(div, newDiv);
      }
    });
  }

  

//checkAndMoveContent();
window.onload = checkAndMoveContent;
//document.body.onchange = checkAndMoveContent;
