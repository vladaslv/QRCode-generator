interface Props {
    zipFile: Blob;
  }
  
  export const DownloadQRCodes: React.FC<Props> = ({ zipFile }) => {
    return <a href={window.URL.createObjectURL(zipFile)} download="qr-codes.zip">
          Download QR Codes
      </a>;
  };