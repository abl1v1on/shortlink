const qr = document.querySelectorAll('.qr-code');
const overlay = document.querySelector('#overlay');
const overlayImage = document.querySelector('#overlay-image');


qr.forEach((image) => {
    image.addEventListener('click', () => {
        overlayImage.src = image.src;
        overlay.classList.add('active');
    })
});

overlay.addEventListener('click', () => {
    overlay.classList.remove('active');
    overlayImage.src = '';
});
