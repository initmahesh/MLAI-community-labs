// DOM Elements
const imageInput = document.getElementById('imageInput');
const output = document.getElementById('output');
const submit = document.getElementById('submit');
const promptInput = document.getElementById('promptInput');

// Configuration
const STABILITY_API_KEY = 'sk-jGokpvKlZIX4PDDMFJXneXaJDzk3trIVQqxu38IMYNEeQomd'; // Replace with your actual API key
const API_URL = 'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image';

// Helper function to log response details
async function logResponseDetails(response) {
    console.log('Response status:', response.status);
    console.log('Response headers:', Object.fromEntries(response.headers.entries()));
    try {
        const clone = response.clone();
        const text = await clone.text();
        console.log('Response body (as text):', text.substr(0, 200) + '...'); // Log first 200 characters
    } catch (e) {
        console.log('Unable to log response body:', e);
    }
}

// Function to display generated images
function displayGeneratedImages(imageUrls) {
    output.innerHTML = ''; // Clear previous images
    imageUrls.forEach(url => {
        const img = document.createElement('img');
        img.src = url;
        img.alt = 'Generated Image';
        img.style.maxWidth = '256px';
        img.style.maxHeight = '256px';
        output.appendChild(img);
    });
}

// Function to resize and crop image
async function resizeAndCropImage(file, targetWidth, targetHeight) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = () => {
            const canvas = document.createElement('canvas');
            canvas.width = targetWidth;
            canvas.height = targetHeight;
            const ctx = canvas.getContext('2d');

            // Calculate scaling and positioning
            const scale = Math.max(targetWidth / img.width, targetHeight / img.height);
            const scaledWidth = img.width * scale;
            const scaledHeight = img.height * scale;
            const offsetX = (targetWidth - scaledWidth) / 2;
            const offsetY = (targetHeight - scaledHeight) / 2;

            // Draw the image on the canvas
            ctx.drawImage(img, offsetX, offsetY, scaledWidth, scaledHeight);

            // Convert canvas to Blob
            canvas.toBlob(resolve, 'image/png');
        };
        img.onerror = reject;
        img.src = URL.createObjectURL(file);
    });
}

// Function to generate image variations
async function generateImageVariations(imageFile, prompt, numVariations = 3) {
    console.log('Generating image variations...');

    // Resize and crop the image to 1024x1024 (you can change this to any of the allowed dimensions)
    const resizedImage = await resizeAndCropImage(imageFile, 1024, 1024);

    const formData = new FormData();
    formData.append('init_image', resizedImage, 'image.png');
    formData.append('init_image_mode', 'IMAGE_STRENGTH');
    formData.append('image_strength', '0.35');

    formData.append('text_prompts[0][text]', prompt);
    formData.append('text_prompts[0][weight]', '1');

    formData.append('cfg_scale', '7');
    formData.append('sampler', 'K_DPM_2_ANCESTRAL');
    formData.append('samples', numVariations.toString());
    formData.append('steps', '30');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${STABILITY_API_KEY}`,
                'Accept': 'application/json'
            },
            body: formData
        });

        await logResponseDetails(response);

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`API error: ${errorData.message}`);
        }

        const result = await response.json();
        return result.artifacts.map(artifact => `data:image/png;base64,${artifact.base64}`);
    } catch (error) {
        console.error('Error generating image variations:', error);
        throw error;
    }
}

// Main demo function
function runDemo() {
    console.log('Demo initialized');

    imageInput.addEventListener('change', (event) => {
        submit.disabled = !event.target.files.length;
    });

    submit.addEventListener('click', async () => {
        if (!imageInput.files.length) {
            alert('Please select an image first.');
            return;
        }

        const file = imageInput.files[0];
        if (!file.type.startsWith('image/')) {
            alert('Please select a valid image file.');
            return;
        }

        const prompt = promptInput.value.trim();

        if (!prompt) {
            alert('Please enter a prompt.');
            return;
        }

        output.textContent = 'Generating image variations...';
        submit.disabled = true;

        try {
            console.log('File details:', file.name, file.type, file.size);

            const variations = await generateImageVariations(file, prompt);
            if (variations.length > 0) {
                displayGeneratedImages(variations);
            } else {
                output.textContent = 'No variations were generated. Please try again.';
            }
        } catch (error) {
            console.error('Error generating image variations:', error);
            output.textContent = 'Failed to generate image variations: ' + error.message;
        } finally {
            submit.disabled = false;
        }
    });

    submit.disabled = !imageInput.files.length;
}

// Run the demo when the DOM is fully loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runDemo);
} else {
    runDemo();
}