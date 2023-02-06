import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'reactstrap';
import * as QRCodeApi from './api/QRCodeApi';
import { DownloadQRCodes } from './components/DownloadQRCodes';
import { QRCodesForm } from './components/QRCodesForm';
import { createFormData } from './utils';


const QRCodeGenerator: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [zipFile, setZipFile] = useState<Blob | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    setLoading(true);
    var formData = createFormData(event, file)

    QRCodeApi.GenerateQRCodes(formData)
    .then((zipFile: React.SetStateAction<Blob | null>) => {
      setZipFile(zipFile);
      setLoading(false);
      setError(null);
    })
    .catch((error: React.SetStateAction<Error | null>) => {
      setError(error);
      setLoading(false);
    });
};

  return (
    <Container>
      <Row className="align-items-center justify-content-center">
        <Col xs={4} style={{ textAlign: 'center' }}>
          <h2>QR Code Generator</h2>
          <QRCodesForm handleSubmit={handleSubmit} handleFileChange={handleFileChange}/>
        {loading && <p>Loading...</p>}
        {error && <p>{error.message}</p>}
        {zipFile && <DownloadQRCodes zipFile={zipFile}/>}
        </Col>
      </Row>
    </Container>
  );
};

export default QRCodeGenerator;