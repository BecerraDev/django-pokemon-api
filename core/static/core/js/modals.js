$(document).ready(function () {

  //- Modal expandir informacion de cartas POKEMON. 
    // Abrir modal con delegación
    $('body').on('click', '.pokemon-item', function () {
      const card = $(this);
      $('#modal-name').text(card.data('name'));
      $('#modal-image').attr('src', card.data('image'));
      $('#modal-types').text(card.data('types'));
      $('#modal-weight').text(card.data('weight'));
      $('#modal-height').text(card.data('height'));
  
      $('#pokemon-modal').removeClass('hidden');
    });
  
    // Cerrar con botón
    $('body').on('click', '#close-modal', function () {
      $('#pokemon-modal').addClass('hidden');
    });
  
    // Cerrar al hacer clic fuera del modal-content
    $('body').on('click', '#pokemon-modal', function (e) {
      if (!$(e.target).closest('.modal-content').length) {
        $(this).addClass('hidden');
      }
    });
  });
  