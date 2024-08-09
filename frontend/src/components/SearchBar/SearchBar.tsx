import styles from "./SearchBar.module.css";

const SearchBar = () => {
  return (
    <input
      type="search"
      placeholder="Busque pelo seu bairro ou cidade"
      width="100%"
      className={styles.searchInput}
    />
  );
};

export default SearchBar;
