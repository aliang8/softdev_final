$('#myTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
})


var addReward = function(e){
    var li = document.createElement("li");
    li.setAttribute("id", "reward")
    li.innerHTML = "<button id='purchase'>hello</button>";
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
}


var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);