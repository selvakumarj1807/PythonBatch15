document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("productForm");

    if (form) {

        form.addEventListener("submit", function (e) {

            e.preventDefault();

            const productId = document.getElementById("productId").value;
            const productName = document.getElementById("productName").value;

            alert(
                `Product Saved Successfully!\n\nID: ${productId}\nName: ${productName}`
            );

            form.reset();
        });

    }

});