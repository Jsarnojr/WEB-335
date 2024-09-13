// Adding a new user to the 'users' collection
db.users.insertOne({
    "firstName": "New",
    "lastName": "User",
    "employeeId": "1013",
    "email": "newuser@example.com",
    "dateCreated": new Date()
  });
  
  // Verify that the new user was added successfully
  db.users.find({ "email": "newuser@example.com" }).pretty();
  // Updating Mozart's email address
db.users.updateOne(
    { "lastName": "Mozart" },
    { $set: { "email": "mozart@me.com" } }
  );
  
  // Verify that the email address was updated successfully
  db.users.find({ "lastName": "Mozart" }).pretty();
 // Displaying all users with projection to show only firstName, lastName, and email
db.users.find({}, { "firstName": 1, "lastName": 1, "email": 1, "_id": 0 }).pretty();
 