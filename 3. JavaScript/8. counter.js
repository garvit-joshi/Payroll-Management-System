let counter = 0;

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});

function count() {
    counter++;

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    }

    document.querySelector('h1').innerHTML = counter;
}

//Use it in HTML:<script src="counter.js"></script> 