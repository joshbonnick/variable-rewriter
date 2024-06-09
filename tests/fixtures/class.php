<?php


class Fruit
{
  public string $name;
  public string $color;
  public int $seeds;

  public function setName($name): void
  {
    $this->name = $name;
  }

  public function get_name(): string
  {
    return $this->name;
  }

  protected function getLabel(): string
  {
      $fruit_name = $this->getName();

      $fruit_label = "$fruit_name fruit";

      return $fruit_label;
  }
}