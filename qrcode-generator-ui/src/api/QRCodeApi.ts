import axios from 'axios';


export const GenerateQRCodes = (payload: any) => {
    return axios.post(process.env.REACT_APP_QRCODES_URL || "", payload, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      responseType: 'blob',
    })
    .then(response => new Blob([response.data]))
};