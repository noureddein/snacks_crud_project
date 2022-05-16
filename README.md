# Lab : 28 - Django CRUD

## In this lab I implemented the following features:

  - Create **snacks_crud_project** Django project
  - Create snacks app
  - Create Snack model
    - title field
    - purchaser field
    - description field
    - Register model with admin
  - Create SnackListView that extends appropriate generic view
    - associated url path is an empty string
  - Create SnackDetailView that extends appropriate generic view
    - associated url path is `<int:pk>/`
  - Create SnackCreateView that extends appropriate generic view
    - associated url path is `create/`
  - Create SnackUpdateView that extends appropriate generic view
    - associated url path is `<int:pk>/update/`
  - Create SnackDeleteView that extends appropriate generic view
    - associated url path is `<int:pk>/delete/`


## Testing
  - Templates:
    - Index view
    - Create snack
    - Delete snack
    - Snack detail
    - Update snack
  - Status code:
    - Index view
    - Create snack
    - Delete snack
    - Snack detail
    - Update snack