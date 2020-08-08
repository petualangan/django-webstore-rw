var updateBtns = document.getElementsByClassName('update-cart') // sesuai sama class css yang di store.html

for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'Action:',action)
    })
}