package example

import java.nio.file.Paths

import org.apache.commons.io.FileUtils

import scala.collection.JavaConverters._
import scala.util.Random

object Main extends App {
  val lines: Seq[String] = (1 to 500)
      .map(_ => Random.nextPrintableChar())
      .grouped(50)
      .map(_.mkString)
      .toSeq

  FileUtils.writeLines(
    Paths.get("out.txt").toFile,
    lines.asJava,
    false
  )
}

