// Adds image viewers to every image in the page

let modal;
let modalImage;

function setVariables()
{
    modal = document.getElementById("modal");
    modalImage = document.getElementById("modal-image");
}

// Executed when the page loads
document.addEventListener("DOMContentLoaded", () => {
    setVariables();
    setEvents();
});

function setEvents()
{
    setOnImageClicked();
    modal.onclick = closeModal;
}

function setOnImageClicked()
{
    const images = [...document.getElementsByTagName("img")];
    for (let i = 0; i < images.length; i++)
    {
        images[i].onclick = (event) => {
            onImageClicked(event.target);
        };
    }
}

function openModal()
{
    modal.style.display = "block";
}

function closeModal(event)
{
    if (event.target != modal)
    {
        return;
    }
    modal.style.display = "none";
}

function setModalImage(image)
{
    modalImage.src = image.src;
    if (image.classList.contains("絵文字"))
    {
        modalImage.style.imageRendering = "pixelated";
    }
    else
    {
        modalImage.style.imageRendering = "auto";
    }
}

function onImageClicked(image)
{
    if (image == modalImage)
    {
        return;
    }
    setModalImage(image);
    openModal();
}
