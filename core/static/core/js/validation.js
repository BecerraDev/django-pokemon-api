 // Función para validar el formulario antes de enviarlo
 function validateForm() {
    // Obtiene y limpia los valores de los inputs
    const name = document.querySelector('input[name="name"]').value.trim();
    const type = document.querySelector('input[name="type"]').value.trim();
    const image = document.querySelector('input[name="image"]').value.trim();

    // Verifica que ningún campo esté vacío
    if (!name || !type || !image) {
      alert("Por favor, completa todos los campos.");  // Muestra mensaje de alerta si falta algo
      return false;  // Detiene el envío
    }

    // Expresión regular para validar que la URL de la imagen sea válida (formato de imagen)
    const urlPattern = /^(https?:\/\/.*\.(?:png|jpg|jpeg|gif|webp))$/i;
    if (!urlPattern.test(image)) {
      alert("Por favor, ingresa una URL válida para la imagen.");  // Muestra error si la URL no es válida
      return false;  // Detiene el envío
    }

    return true;  // Si todo está correcto, devuelve true
  }

  // Función para mostrar un mensaje flotante mientras se envía el formulario
  function showAddingMessage(form) {
    const message = document.createElement('div');  // Crea un nuevo elemento <div>
    message.innerText = 'Agregando Pokémon...';     // Texto que se mostrará

    // Estilo del mensaje usando clases de Tailwind (posición fija, centrado, fondo verde, etc.)
    message.className = 'fixed top-5 left-1/2 transform -translate-x-1/2 bg-green-100 text-green-800 px-4 py-2 rounded shadow z-50';
    document.body.appendChild(message);  // Añade el mensaje al body

    // Espera 150ms antes de enviar el formulario (puede ser útil para mostrar animaciones o loaders)
    setTimeout(() => {
      form.submit();  // Envía el formulario
    }, 150);
  }

  // Función que se llama al enviar el formulario (por ejemplo, onsubmit="return handleFormSubmit(this)")
  function handleFormSubmit(form) {
    if (!validateForm()) {
      return false;  // Si la validación falla, detiene el envío
    }

    showAddingMessage(form);  // Muestra el mensaje "Agregando Pokémon..."
    return false;  // Previene el envío inmediato, ya que se hará manualmente después de 150ms
  }