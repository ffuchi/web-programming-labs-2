function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;   
    
    const obj = {
        'method':'get_price',
        'params':{
            drink:drink,
            milk:milk,
            sugar:sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(obj)
      })
        .then(function (resp) {
          return resp.json();
        })
        .then(function (data) {
          document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
          document.querySelector('#pay').style.display = '';
        });
}


function pay(){
    const drink = document.querySelector('[name=drink]:checked').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        'method':'pay',
        'params':{
            drink:drink,
            milk:milk,
            sugar:sugar,
            card_num:card,
            cvv:cvv
        }
    }
    
    fetch('/lab7/api',{
            method:'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify(obj)
        })
        .then(function(resp){
            return resp.json();
        })
        .then(function(data){
            if (data.error) {
                document.querySelector('#error').innerHTML = data.error;
            } else {
                document.querySelector('#result').innerHTML = data.result;
                document.querySelector('#refund').style.display='';
            }
        })
}


function refund(){
    const drink = document.querySelector('[name=drink]:checked').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const card = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    
    const obj = {
        'method':'refund',
        'params':{
            drink:drink,
            milk:milk,
            sugar:sugar,
            card_num:card,
            cvv:cvv
        }
    }

    fetch('/lab7/api',{
        method:'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        if (data.error) {
            document.querySelector('#error').innerHTML = data.error;
        } else {
            document.querySelector('#result').innerHTML = data.result;
            document.querySelector('#refund').style.display='';
        }
    })
}