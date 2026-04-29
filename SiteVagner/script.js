let currentIndex = 0;
let modalImages = [];

function moveCarousel(direction) {
  const track = document.getElementById('carouselTrack');
  const items = track.querySelectorAll('.carousel-item');
  const itemWidth = items[0].offsetWidth + 24;
  const visible = Math.floor(track.parentElement.offsetWidth / itemWidth);
  const max = items.length - visible;

  currentIndex = currentIndex + direction;

  if (currentIndex > max) currentIndex = 0;
  if (currentIndex < 0) currentIndex = max;

  track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
}

function openModal(img) {
  modalImages = Array.from(document.querySelectorAll('.carousel-item img'));
  currentModalIndex = modalImages.indexOf(img);

  document.getElementById('modalImg').src = img.src;
  document.getElementById('modal').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function changeModalImg(direction) {
  currentModalIndex = (currentModalIndex + direction + modalImages.length) % modalImages.length;
  document.getElementById('modalImg').src = modalImages[currentModalIndex].src;
}


function closeModal(e) {
  if (e.target === document.getElementById('modal')) {
    document.getElementById('modal').classList.remove('active');
    document.body.style.overflow = '';
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    document.getElementById('modal').classList.remove('active');
    document.getElementById('modalOrc').classList.remove('active');
    document.body.style.overflow = '';
  }
  if (e.key === 'ArrowLeft') changeModalImg(-1);
  if (e.key === 'ArrowRight') changeModalImg(1);
});

function openModalOrc(e) {
  e.preventDefault();
  document.getElementById('modalOrc').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModalOrc(e) {
  if (e.target === document.getElementById('modalOrc')) {
    document.getElementById('modalOrc').classList.remove('active');
    document.body.style.overflow = '';
  }
}

function forceCloseModalOrc() {
  document.getElementById('modalOrc').classList.remove('active');
  document.body.style.overflow = '';
  document.querySelector('.modalForm').reset();
}

function maskPhone() {
  const input = document.querySelector('input[placeholder^="(11)"]');
  let value = input.value.replace(/\D/g, ''); // remove tudo que não é número

  if (value.length > 11) value = value.slice(0, 11);

  if (value.length <= 10) {
    // Formato: (11) 1111-1111
    value = value
      .replace(/^(\d{2})/, '($1) ')
      .replace(/(\d{4})(\d)/, '$1-$2');
  } else {
    // Formato: (11) 11111-1111
    value = value
      .replace(/^(\d{2})/, '($1) ')
      .replace(/(\d{5})(\d)/, '$1-$2');
  }

  input.value = value;
}

// Fecha com ESC
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') document.getElementById('modalOrc').classList.remove('active');
});