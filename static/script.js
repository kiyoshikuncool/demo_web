document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  // Đăng nhập
  if (loginForm) {
    loginForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const email = loginForm.email.value;
      const password = loginForm.password.value;

      try {
        const response = await fetch("/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.message || "Login failed");
        }

        console.log("Login success:", data);
        window.location.href = "/dashboard";
      } catch (error) {
        console.error("Login error:", error.message);
        alert("❌ Đăng nhập thất bại: " + error.message);
      }
    });
  }

  // Đăng ký
  if (registerForm) {
    registerForm.addEventListener("submit", async function (e) {
      e.preventDefault();

      const name = registerForm.name.value;
      const email = registerForm.email.value;
      const password = registerForm.password.value;
      const role = registerForm.role.value;
      console.log(role)

      try {
        const response = await fetch("/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ name, email, password, role }),
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.message || "Register failed");
        }

        console.log("Register success:", data);
        alert("✅ Đăng ký thành công! Bạn có thể đăng nhập.");
        window.location.href = "/index"; // về trang login
      } catch (error) {
        console.error("Register error:", error.message);
        alert("❌ Đăng ký thất bại: " + error.message);
      }
    });
  }
});
