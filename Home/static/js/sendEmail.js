const sendEmail = () => {
    const server_id = "service_gyc7adf";
    const template_id = "template_31bxose";

    let paras = {
        subject : "📬 An email from your client.",
        email : document.getElementById("email").value,
        name: `${document.getElementById("firstName").value} ${document.getElementById("lastName").value}`,
        message:`Client📱: ${document.getElementById("phone").value}. 
                 Message👨‍💻 : ${document.getElementById("message").value}`
    };

    emailjs.send(server_id,template_id,paras);
};


