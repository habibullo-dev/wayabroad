fetch("/blog/data")
  .then((response) => response.json())
  .then((data) => {
    // Populate the main blog post
    const mainPost = data[0];
    let mainPostName = mainPost["Blog name"].replace(/[?!]/g, "");
    document.querySelector("#post-title").textContent = mainPost["Blog name"];
    document.querySelector("#post-date").textContent = mainPost["Date"];
    document.querySelector("#post-tags").textContent =
      mainPost["Hashtags"].join(" ");
    document.querySelector(
      "#post-image"
    ).src = `./static/img/blog/${mainPostName}.jpg`;

    // Divide the content into sections
    let mainPostContent = mainPost["Blog content"].split(".");
    document.querySelector("#post-content").innerHTML = `
  <h2>${mainPostContent[0]}.</h2>
  <p>${mainPostContent.slice(1, mainPostContent.length).join(".")}</p>
`;

    // Populate the featured blogs
    const featuredBlogs = data.slice(1); // Get all other blogs
    const featuredBlogsContainer = document.querySelector(".card-body");
    featuredBlogs.forEach((blog, index) => {
      let blogName = blog["Blog name"].replace(/[?!]/g, "");
      // Create new HTML elements for each blog
      const blogElement = document.createElement("div");
      blogElement.innerHTML = `
        <img class="img-fluid rounded" src="./static/img/blog/${blogName}.jpg" alt="Image of ${
        blog["Blog name"]
      }">
        <h2 class="mt-2">${blog["Blog name"]}</h2>
        <h3>${blog["Blog content"].split(".")[0] + "."}</h3>
        <p>${blog["Blog content"].split(".")[1] + "."}</p>
        <p>${blog["Blog content"].split(".")[2] + "."}</p>
        <a href="" class="btn btn-primary">Learn More</a>
      `;
      blogElement.classList.add("mb-4");
      blogElement.querySelector(".btn").addEventListener("click", (event) => {
        event.preventDefault(); // Prevent the default action
        // Replace the main blog post with the clicked featured blog
        document.querySelector("#post-title").textContent = blog["Blog name"];
        document.querySelector("#post-date").textContent = blog["Date"];
        document.querySelector("#post-tags").textContent =
          blog["Hashtags"].join(" ");
        document.querySelector(
          "#post-image"
        ).src = `./static/img/blog/${blogName}.jpg`;
        document.querySelector("#post-content").textContent =
          blog["Blog content"];
        // Add a shadow box to the active blog and remove it from others
        document
          .querySelectorAll(".card-body > div")
          .forEach((el) => (el.style.boxShadow = ""));
        blogElement.style.boxShadow = "0 0 20px rgba(0, 0, 0, 0.8)";
      });
      // Add the new blog element to the container
      featuredBlogsContainer.appendChild(blogElement);
    });
  });
