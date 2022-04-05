

var updateBtns = document.get.ElementByClassName('update-cart')

for(var i=0; i < updateBtns.lengt; i++){
    uodateBtns[i].addEventListener('click, function(){
        var prodcutId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        })
}


var updateBtns = document.getElementsByClassName('update-cart')


for(var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        })
}