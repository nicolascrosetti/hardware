document.addEventListener('DOMContentLoaded', function() {
    const listingButtons = document.querySelectorAll('.listing-btn');

    //Modals para productos
    listingButtons.forEach(button => {
        button.addEventListener(("click"), () =>{
            const modalContainer = document.querySelector(`.modal-container[data-id="${button.dataset.id}"]`);
            const modal = document.querySelector(`.modal-container[data-id="${button.dataset.id}"] .modal`);
            const closeModal = modal.querySelector(`.close-modal-button`);

            modalContainer.classList.remove("hidden");
            modal.classList.remove("hidden");
            setTimeout(() => {
                modal.classList.remove('opacity-0');
            }, 10);

            closeModal.addEventListener('click', () => {
                modalContainer.classList.add('hidden');
                modal.classList.add('hidden');
                modal.classList.add('opacity-0');
            });
        });
    });

    //Modal para mensaje de exito en formulario de contacto
    const modalMessageContainer = document.querySelector(`.modal-message-container`);
    const modalMesssage = document.querySelector(`.modal-message-container .modal-message`);
    const closeModalMessage = modalMesssage.querySelector(`.close-modal-button`);

    closeModalMessage.addEventListener('click', () => {
        modalMessageContainer.classList.add('hidden');
        modalMesssage.classList.add('hidden');
    });


});