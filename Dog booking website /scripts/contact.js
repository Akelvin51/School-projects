// when the "submit-button" is clicked, the contents of the contact-page are replaced with a single <p> element that reads "Thank you for your message" in size 24 font.

// hint: you can change the style of an element by modifying the value of that element's .style.fontSize, or by updating its .classList.

// Get the submit button and the contact page
const submitButton = document.querySelector('#submit-button');
const contactPage = document.querySelector('#contact-page');

// Add an event listener to the submit button
submitButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  // Replace the contents of the contact page with the thank you message
  contactPage.innerHTML = '<p>Thank you for your message</p>';
  contactPage.style.fontSize = '24px';
});
