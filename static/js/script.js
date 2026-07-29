console.log("Student Management System Loaded");
let forms=document.querySelectorAll("form");
forms.forEach(function(form){
    form.addEventListener("submit",function(e){
        let inputs=form.querySelectorAll("input[required],select[required]");
        for(let input of inputs){
            if(input.value.trim()==""){
                alert("Please fill all the fields.");
                e.preventDefault();
                return;
            }
        }
    });
});