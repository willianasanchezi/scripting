const PDFDocument = require('pdfkit');  
const fs = require('fs');  
  
// Crear un nuevo documento PDF  
const doc = new PDFDocument();  
  
// Guardar el documento en un archivo  
doc.pipe(fs.createWriteStream('output.pdf'));  
  
// Agregar el primer párrafo  
doc.fontSize(12).text('Este es el primer párrafo antes de la imagen.', {  
  align: 'left',  
  paragraphGap: 10  
});  
  
// Obtener la posición actual del cursor  
let y = doc.y;  
console.log(y);  
  
// Ruta y dimensiones de la primera imagen  
const imagePath1 = 'bird-9432600_640.jpg';  
const imageWidth1 = 250; // Ajusta este valor según el ancho de tu imagen  
const imageHeight1 = 300; // Ajusta este valor según el alto de tu imagen  
  
// Agregar la primera imagen en una posición específica  
doc.image(imagePath1, 100, y + 10, {  
  fit: [imageWidth1, imageHeight1],  
  align: 'center'  
});  
  
// Actualizar la posición del cursor de escritura para estar debajo de la primera imagen  
doc.y = y + imageHeight1 + 20; // Ajusta este valor según sea necesario  
console.log(doc.y);  
  
// Agregar el segundo párrafo debajo de la primera imagen  
doc.fontSize(12).text('Este es el segundo párrafo después de la primera imagen.', {  
  align: 'left',  
  paragraphGap: 10  
});  
  
// Agregar el tercer párrafo  
doc.fontSize(12).text('Este es el tercer párrafo después de la primera imagen.', {  
  align: 'left',  
  paragraphGap: 10  
});  
console.log(doc.y);  
  
// Obtener la posición actual del cursor para la segunda imagen  
y = doc.y;  
  
// Ruta y dimensiones de la segunda imagen  
const imagePath2 = 'bird-9432600_640.jpg'; // Reemplaza esto con la ruta correcta a tu segunda imagen  
const imageWidth2 = 250; // Ajusta este valor según el ancho de tu segunda imagen  
const imageHeight2 = 300; // Ajusta este valor según el alto de tu segunda imagen  
  
// Agregar la segunda imagen en una posición específica  
doc.image(imagePath2, 100, y + 10, {  
  fit: [imageWidth2, imageHeight2],  
  align: 'center'  
});  
  
// Actualizar la posición del cursor de escritura para estar debajo de la segunda imagen  
doc.y = y + imageHeight2 + 20; // Ajusta este valor según sea necesario  
console.log(doc.y);  
  
// Finalizar el documento  
doc.end();  
  
console.log('El documento PDF se ha creado.');  