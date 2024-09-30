const form = document.getElementById('uploadForm')
form.addEventListener('submit', async function(event) {
    event.preventDefault();
    console.log(event);
    console.log('Posting Message: ');
    const formData = new FormData();
    const form_k = document.getElementById('k');
    const form_init = document.getElementById('init');
    const form_button = document.getElementById('button_type');
    

    formData.append('form_k', form_k.value);
    formData.append('form_init', form_init.value);
    formData.append('form_button', form_button.value);

    const response = await fetch('/makegraph', {
        method: 'POST',
        body: formData,
    });

    const data = await response.json();

    // Now that we have data, must render it in a graph
    const graphContainer = document.getElementById('graphContainer');
    graphContainer.innerText = JSON.stringify(data)
});
