


document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#sub_pseudo').disabled = true;

    if(localStorage.getItem('pseudo'))
      {
        var pseudo =localStorage.getItem('pseudo');
        document.querySelector('h1').innerHTML =`Welcome back ${pseudo} !!`;
      }
    // Enable button only if there is text in the input field
    document.querySelector('#tbo_pseudo').onkeyup = () => {
        if (document.querySelector('#tbo_pseudo').value.length > 0)
            document.querySelector('#sub_pseudo').disabled = false;
        else
            document.querySelector('#sub_pseudo').disabled = true;
    };

    document.querySelector('#frm_pseudo').onsubmit = () => {
        var pseudo=document.querySelector('#tbo_pseudo').value;
        localStorage.setItem('pseudo',pseudo);
        document.querySelector("#message").innerHTML = `Hello ${pseudo}, now you can start conversation *_*`;
        // Stop form from submitting
        return false;
    };

});
