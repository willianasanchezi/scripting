const PDFDocument = require('pdfkit');
const fs = require('fs');

// Crear un documento PDF
const doc = new PDFDocument({ size: 'LETTER' });

// Guardar el PDF en un archivo
doc.pipe(fs.createWriteStream('documento.pdf'));

// Agregar contenido
doc.fontSize(20).text('Test');
doc.moveDown();

//Parrafo
const lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";

doc.fontSize(8);
doc.text(`This text is left aligned. ${lorem}`, {
width: 410,
align: 'left'
}
);
doc.moveDown();
doc.text(`This text is centered. ${lorem}`, {
width: 410,
align: 'center'
}
);
doc.moveDown();

doc.text(`This text is right aligned. ${lorem}`, {
width: 410,
align: 'right'
}
);

doc.moveDown();
doc.text(`This text is justified. ${lorem}`, {
width: 410,
align: 'justify'
}
);
doc.moveDown();

// Insertar una imagen
doc.image('bird-9432600_640.jpg', 100, 250, { width: 200 });
doc.moveDown();

doc.fontSize(14).text('Este es un documento PDF generado con Node.js.');
// Finalizar el documento
doc.end();

console.log('PDF creado: documento.pdf');

//https://pdfkit.org/docs/text.html