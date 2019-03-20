<template>
  <div class="book">
    <div class="description">
      <div class="basic-info">
        <div class="title">
          <span class='field-name'>Title: </span>
          <span class='field-value'>Harry Potter and the Philosopher's Stone</span>
        </div>
        <div class="author">
          <span class="field-name">Author: </span>
          <span class="field-value">J. K. Rowling</span>
        </div>
        <div class="isbn">
          <span class="field-name">ISBN: </span>
          <span class="field-value">0747532699</span>
        </div>
      </div>
      <p class="availability">AVAILABLE</p>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['title', 'author', 'isbn', 'availability'],
  }
</script>

<style scoped>
  .book {
    margin-top: 3rem;
    padding: 2rem;
    background-image: linear-gradient(to bottom right, #f5cd79, #e15f41);
  }
  .description {
    display: flex;
    align-items: center;
    justify-content: space-around;
  }
  .basic-info {
    width: 50%;
  }
  .availability {
    padding: 1rem 2rem;
    margin-left: auto;
    text-transform: uppercase;
    background-color: white;
    border-radius: 3px;
    width: 10rem;
    display: flex;
    justify-content: center;
  }
</style>
