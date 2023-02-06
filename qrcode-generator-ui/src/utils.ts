
export const createFormData = (event: React.FormEvent<HTMLFormElement>, logo: File | null) => {
    const formData = new FormData();
    if (logo) {
      formData.append('logo', logo, logo.name);
    }
  
    const id_suffix = (event.target as HTMLFormElement).id_suffix.value;
    formData.append('suffix', id_suffix);
    const id_prefix = (event.target as HTMLFormElement).id_prefix.value;
    formData.append('prefix', id_prefix);
    const id_zeros = (event.target as HTMLFormElement).id_zeros.value;
    formData.append('zeros', id_zeros);
    const amount = (event.target as HTMLFormElement).amount.value;
    formData.append('amount', amount);
  
    return formData;
  };