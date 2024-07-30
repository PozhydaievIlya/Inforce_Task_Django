Functionality of a project:

✔ Authentication

    ♦ Session Authentication
       Usage
       Login on /api/auth/login/
       Logout on /api/auth/logout/

    ♦ JWT token
       Usage
       Register: Send a POST request to /api/register/ with username, password, and email to create a new user.
       Login: Send a POST request to /api/login/ with username and password to obtain JWT tokens.
       Token Refresh: Send a POST request to /api/token/refresh/ with the refresh token to obtain a new access token.
       Get User Info: Send a GET request to /api/user/ with a valid access token to retrieve user information.


✔ Creating restaurant

    api/restaurants/ - all restaurants list (read-only)
    api/restaurants/ - create and view restaurants
    api/restaurants/<int:pk>/ - restaurant detail with Update and Delete functions (Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS)

✔ Uploading menu for restaurant

    api/menu/ - all menu list (read-only)
    api/menu/create/ -  create and view menu 
    api/menu/<int:pk>/ - menu detail with Update and Delete functions (Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS)

✔ Creating employee

    api/employees/ - all employee list (read-only)
    api/employees/create/ - create and view employees
    api/employees/<int:pk>/ - employee detail with Update and Delete functions (Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS)

✔ Getting current day menu

    api/menu/today/ - getting current day menu

✔ POSTGRESQL used

    if do not work -> uncomment sqlite3 database in inforse_py_task/settings.py and comment POSTGRESQL section
