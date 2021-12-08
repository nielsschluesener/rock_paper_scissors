var picForm = document.querySelector('form');

picForm.addEventListener('submit', event => {
    event.preventDefault();

    console.log('shutter_triggered');

    var timer = document.getElementById('shutter_btn');
    var title = document.getElementById('title');
    var explanation = document.getElementById('explanation');

    timer.setAttribute('disabled', 'disabled');
    timer.style.fontSize = "2.2rem";
    timer.innerHTML = 5;

    title.style.color = '#fff';
    explanation.style.color = '#fff';

    document.body.style.backgroundColor = '#1BD2B2';



    var countdown = window.setInterval(function () {



        var seconds = timer.innerHTML;
        seconds = seconds - 1;
        timer.innerHTML = seconds;

        if (seconds == 0) {

            document.body.style.transition = "all .2s";
            document.body.style.backgroundColor = '#fff';

            timer.innerHTML = 'Cheese!';

            clearInterval(countdown);
        }

    }, 1000);

    window.setTimeout(function () {

        console.log('play_sound');

        var audio = new Audio('static/assets/sfx/shutter_sfx.wav');
        audio.play();

        window.setTimeout(function () {

            document.body.style.backgroundColor = '#1BD2B2';

            window.setTimeout(function () {

                picForm.submit();
                console.log('form_submitted');

            }, 600);

        }, 350);

    }, 5000);

});