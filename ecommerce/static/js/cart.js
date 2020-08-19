var updateBtns = document.getElementsByClassName('update-cart') // sesuai sama class css yang di store.html

for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'Action:',action) // diconsole nanti, muncul id sama actionnya | action -> store.html -> data-action="add"

        console.log('USER:', user)
        if (user == 'AnonymousUser'){ //kalau user belum login
            addCookieItem(productId, action)
        }else{ // kalau user udah login
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // csrftoken dapet dari main.html
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
        .then((response) => { // ini promise. masih belum tau itu apaan
            return response.json();
        })
        .then((data) => {
             console.log('Data:', data)
             location.reload() // update angka di logo keranjang
        });

}

// fungsi yang berjalan kalau user belum login
function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if(action == 'add'){    // menambah product kalau actionnya add
		if (cart[productId] == undefined){
			cart[productId] = {'quantity':1}
		}else{
			cart[productId]['quantity'] += 1
		}
	}
	if(action == 'remove'){
		cart[productId]['quantity'] -= 1

		if(cart[productId]['quantity'] <= 0){ // kalau kurang dari satu, delete product
			console.log('Item should be deleted')
			delete cart[productId]
		}
	}
	console.log('CART:', cart)
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}