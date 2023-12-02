var my_card = document.querySelector("#card");
var userName = "";

function getUserName(element){
    console.log(element.value)
    userName=element.value

}

function displayUserInfo(data){
    var result=
    `
    <div class="card p-2  col-5 text-center mx-auto ">
        <div class="card-header bg-warning mb-1">
            <h5><strong>${data.name}</strong> has <strong> ${data.followers}</strong> followers <h5> 
        </div>
        <img src="${data.avatar_url}" class="card-img-body mb-1" alt="${data.login}>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">Location: ${data.location}</li>
            <li class="list-group-item">Repositories: ${data.public_repos}</li>
        </ul>
    <div>
    `
    console.log(result)
    return result
}


async function searchGit(){
    var response=await fetch(" https://api.github.com/users/" + userName)
    var all_data=await response.json()
    console.log(all_data)
    my_card.innerHTML=displayUserInfo(all_data)
    return my_card
    
}
