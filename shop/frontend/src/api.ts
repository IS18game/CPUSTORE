export async function fetchData(endpoint: string) {
  const response = await fetch(endpoint);
  if (!response.ok) {
    throw new Error('Ошибка загрузки данных');
  }
  return response.json();
}
