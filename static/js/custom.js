$('#myTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
})

var removeReward = function(e){
    this.parentNode.remove();
}

var addReward = function(e){
    var li = document.createElement("li");
    li.setAttribute("id", "reward")
    var name = document.getElementById("reward_name");
    name = name.value;
    var price = document.getElementById("reward_cost");
    price = price.value;
    li.innerHTML = "Reward: " + name + " Price: " + price + "<button class='purchase'>Purchase</button>";
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
    var reward_list = document.getElementById("rewards");
    var rewards = reward_list.getElementsByClassName("purchase");
    for(i=0; i < rewards.length; i++){
	rewards[i].addEventListener("click", removeReward);

    }

}
var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);


var addToDo = function(e){
  
  var item = document.createElement("li");
  var.class = "todoitem";
  
  
  
}
