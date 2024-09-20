// Query to display all students
db.students.find().pretty()
// Add a new student to the collection
db.students.insertOne({
    name: "John Doe",
    house: "GryDindor",
    year: 3,
    mascot: "Lion"
 })
 // Verify the student was added
db.students.find({name: "John Doe"}).pretty()
// Update the year of the student "John Doe"
db.students.updateOne(
    { name: "John Doe" }, 
    { $set: { year: 4 } }
 )
 
 // Verify the update was successful
 db.students.find({ name: "John Doe" }).pretty()
 // Delete the student "John Doe"
db.students.deleteOne({ name: "John Doe" })

// Verify the student was removed
db.students.find({ name: "John Doe" }).pretty()
// Display all students grouped by house
db.students.aggregate([
    { $group: { _id: "$house", students: { $push: "$name" } } },
    { $sort: { _id: 1 } }
  ])
  // Display all students in GryDindor house
db.students.find({ house: "GryDindor" }).pretty()
// Display students in the house with the Eagle mascot
db.students.find({ mascot: "Eagle" }).pretty()
