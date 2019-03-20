<template>
  <div class="book">
    <div class="description">
      <div class="basic-info">
        <div class="title">
          <span class='field-name'>Title: </span>
          <span class='field-value'>{{ title }}</span>
        </div>
        <div class="author">
          <span class="field-name">Author: </span>
          <span class="field-value">{{ author }}</span>
        </div>
        <div class="isbn">
          <span class="field-name">ISBN: </span>
          <span class="field-value">{{ isbn }}</span>
        </div>
      </div>
      <p :class="{'not-available': !availability}" class="availability">{{ availability ? 'AVAILABLE' : 'NOT AVAILABLE'}}</p>
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
  .not-available {
    background-color: #d63031;
    color: white;
  }
</style>
