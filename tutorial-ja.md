% Rust 言語チュートリアル (非公式日本語訳)

# イントロダクション

## 範囲

これは Rust プログラミング言語のチュートリアルです。読者はプログラミングの基本
的な概念に慣れていて、一つ以上、他言語でプログラミング経験があると仮定していま
す。しばし C 系統の他言語と比較を行います。このチュートリアルは言語全体をカバー
しますが、[言語仕様書](rust.html)ほどの深さと正確さはありません。

## 言語の概要

Rust は、型安全性、メモリ安全性、並列性、パフォーマンスに焦点を置いたシステムプ
ログラミング言語です。 C++ のような言語でよく起こるある種のエラーを避けつつ、大
規模で高パフォーマンスのアプリケーションを書くことに向いています。 Rust は洗練
されたメモリモデルを持っており、 C++ で使われるようなたくさんの効率的なデータ構
造を利用可能にすると同時に、セグメンテーション違反を起こす無効なメモリアクセス
を禁止します。他のシステム言語のように、静的に型付けされ、事前コンパイル (ahead
of time compilation) されます。

マルチパラダイム言語として、Rust は手続き的、関数的、オブジェクト指向的なスタイ
ルでコードを記述することをサポートします。 Rust の素敵で高レベルな特徴として、
次のようなものがあります。

* ***パターンマッチングおよび代数的データ型 (enum) 。*** 関数型言語でよく使われ
  ているもので、 ADT のパターンマッチングはプログラムのロジックを記述するための、
  簡潔で表現しやすい方法を提供します。
* ***タスクベース並列性。*** - Rust はメモリを共有しない軽量なタスクを用います。
* ***高階関数。*** Rust の関数は引数としてクロージャをとったり、返り値としてク
  ロージャを返すことが可能です。 Rust のクロージャはとてもパワフルで、いたる所
  で使われます。
* ***trait 多相性。*** Rust の型システムは _trait_ と呼ばれる、 Java スタイルの
  インターフェイスと、 Haskell スタイルの型クラスのユニークな組み合わせを特徴と
  しています。
* ***パラメータ多相性 (generics) 。*** 関数と型は、オプショナルな型制約を伴う型
  変数でパラメータ化できます。
* ***型推論。*** ローカル変数の宣言での型注釈 (type annotation) は省略可能です。

## ファーストインプレッション

C, C++, JavaScript の伝統を受け継いだ波括弧を多用する言語として、 Rust は読者が
慣れ親しんでいる他の言語と見た目がよく似ています。

~~~~
fn boring_old_factorial(n: int) -> int {
    let mut result = 1, i = 1;
    while i <= n {
        result *= i;
        i += 1;
    }
    return result;
}
~~~~

いくつか C と異なる部分が現れています。型は変数名の前ではなく後に置かれ、前にコ
ロンが付きます。 `let` で導入されるローカル変数では型を省略可能で、省略した場合
は推論されます。 `while` や `if` のような構文では条件式を囲む括弧は必要ありませ
ん (囲うことも許されます) 。

しかし、 Rust が単純な C の発展形であると結論しないでください。このチュートリア
ルで明らかになるように、 Rust はたくさんの高レベルなイディオムのために、効率的
で、強い型付けを持ち、メモリ安全性をサポートするという、全く違う方向性を持ちま
す。

## 慣例

このチュートリアル全体を通して、言語のキーワードを示す単語やコード例の中で定義
される識別子を `code font` で記述します。

コード片はインデントされ、固定幅フォントで記述されます。コード片がプログラム全
体を構成するとは限りません。簡潔さのため、それ自身はコンパイルできないプログラ
ムの断片を見せることがあります。試してみるためには、そのコードを
`fn main() { ...  }` で囲う必要があるかもしれません。また、実際に定義されていな
いものへの参照を含まないことを確認してください。

> ***警告:*** Rust は非常に開発途上の言語です。言語の変更や実装の欠如の可能性、
> その他ブロッククォート上で示される警告に注意してください。

# げてぃん・すたーてっ

## インストール

Rust コンパイラは現在のところ [tarball][] からビルドする必要があります。将来的
にはたくさんの OS に対しバイナリパッケージを配布しようと思っています。

Rust コンパイラはそれ自身が Rust で書かれているため、 (開発のより前の段階で作ら
れた) コンパイル済みの「スナップショット」バージョンでビルドする必要があるとい
う点が、少しだけ通常と異なります。ソースビルドには次のものが必要です。

  * スナップショットをダウンロードするするため、インターネットに接続されている
	こと。
  * 我々が提供しているスナップショットバイナリのどれかを実行できること。
    * Windows (7, server 2008 r2), x86 のみ
    * Linux (various distributions), x86 と x86-64
    * OSX 10.6 ("Snow Leopard") または 10.7 ("Lion"), x86 と x86-64

この他のプラットフォームでも動作するかもしれませんが、最も動作する可能性の高い、
"tier 1" としてサポートされるビルド環境が存在します。将来、クロスコンパイルによっ
てさらに多くのプラットフォームが加えられるでしょう。

ソースからビルドするには、次のパッケージが必要です。

  * g++ 4.4 or clang++ 3.x
  * python 2.6 or later
  * perl 5.0 or later
  * gnu make 3.81 or later
  * curl

あなたが比較的新しい *nix を使っていて上の条件を満たしていれば、だいたいうまく
いくはずです。 Windows 上でソースからビルドするには追加の手順が必要です。 Rust
wiki の [getting started][wiki-get-started] を参照してください。

~~~~ {.notrust}
$ wget http://dl.rust-lang.org/dist/rust-0.3.tar.gz
$ tar -xzf rust-0.3.tar.gz
$ cd rust-0.3
$ ./configure
$ make && make install
~~~~

インストール先のディレクトリを修正する権限がない場合、 `sudo make install` を使
う必要があるかもしれません。インストール先は `configure` に引数 `--prefix` を渡
すことで変更できます。他のいろいろなオプションもサポートされています。詳細を知
りたいときは `--help` を渡してください。

ビルドが完了すれば、 `make install` で次のプログラムが `/usr/local/bin` にイン
ストールされます。

  * `rustc`, Rust コンパイラ
  * `rustdoc`, API ドキュメンテーションツール
  * `cargo`, Rust パッケージマネージャ

[wiki-get-started]: https://github.com/mozilla/rust/wiki/Note-getting-started-developing-Rust
[tarball]: http://dl.rust-lang.org/dist/rust-0.3.tar.gz

## 最初のプログラムをコンパイルする

Rust のプログラムファイルは、慣例として拡張子 `.rs` が与えられます。次の内容の
ファイル `hello.rs` があるとします。

~~~~
fn main() {
    io::println("hello world!");
}
~~~~

Rust コンパイラが正しくインストールされていれば、 `rustc hello.rs` を実行すると
`hello` (もしくは `hello.exe`) というバイナリが生成されるはずです。

もしこのプログラムを不正になるように修正し (例えば、 `io::println` を何か存在し
ない関数に換える) 、コンパイルしたら、次のようなエラーメッセージが表示されるで
しょう。

~~~~ {.notrust}
hello.rs:2:4: 2:16 error: unresolved name: io::print_it
hello.rs:2     io::print_it("hello world!");
               ^~~~~~~~~~~~
~~~~

Rust コンパイラはエラーに出くわしたとき、役立つ情報を提供しようとします。

## Rust プログラムの構造

一番単純な形式の Rust プログラムは、いくつかの型と関数が定義されている `.rs` フ
ァイルです。もし `main` 関数が存在すれば、実行形式にコンパイルできます。 Rust
は、宣言でないコードがファイルのトップレベルに現れることを許しません。つまり、
全てのステートメントは関数内になければいけません。

Rust プログラムはライブラリとしてもコンパイルでき、他のプログラムにインクルード
され得ます。
多く例の一番上に現れる `extern mod std` ディレクティブは、[標準ライブラリ][std]
をインポートします。これについては[後ほど](#modules-and-crate)より詳細に記述し
ます。

[std]: http://doc.rust-lang.org/doc/std

## Rust コードの編集

Rust のソース配布物の `src/etc/vim/` に Vim のハイライトとインデントを行うスク
リプトが、また `src/etc/emacs/` に emacs mode があります。 Sublime Text 2 のた
めのパッケージが
[github.com/dbp/sublime-rust](http://github.com/dbp/sublime-rust) にあり、
[package control](http://wbond.net/sublime_packages/package_control) からも利用
可能です。

他のエディタ向けのものはまだ提供されていません。もしあなたが好きなエディタ向け
の Rust モードを書いたら、私たちがリンクできるよう知らせてください。

# 構文の基本

## ブレース

あなたが C 系統の言語 (C++, Java, JavaScript, C#, PHP) でプログラムしたことがあ
れば、 Rust は親しみやすく感じられるでしょう。主な表面的な違いは、 `if` ステー
トメントと `while` ループの本体をブラケットで囲む*必要がある*ということです。単一
のステートメントであっても、ブラケットで囲われていない本体は許されません。

これらの違いを理解すれば、 Rust のステートメントと式の表面的な構文は C ライクで
す。関数呼び出しは `myfunc(arg1, arg2)` と記述され、演算子は C とおおむね同じ名
前と優先順位を持ち、コメントは同じであり、 `if` や `while` のような構文が利用で
きます。

~~~~
# fn it_works() {}
# fn abort() {}
fn main() {
    while true {
        /* Ensure that basic math works. */
        if 2*20 > 30 {
            // Everything is OK.
            it_works();
        } else {
            abort();
        }
        break;
    }
}
~~~~

## 式の構文

全てのコード上で明白なわけではありませんが、 Rust の構文と C 系統の先行する言語
との間には基本的な違いがあります。 C ではステートメントであるたくさんの構成物が、
Rust では式です。これは Rust をより表現豊かにします。例えば、あなたは次のような
コードを書いたことがあるかもしれません。

~~~~
# let item = "salad";
let price;
if item == "salad" {
    price = 3.50;
} else if item == "muffin" {
    price = 2.25;
} else {
    price = 2.00;
}
~~~~

しかし Rust では名前 `price` をくり返す必要はありません。

~~~~
# let item = "salad";
let price = if item == "salad" { 3.50 }
            else if item == "muffin" { 2.25 }
            else { 2.00 };
~~~~

二つのコードは厳密に等価です。つまり、条件に依って `price` に値を代入します。二
つ目のコードからセミコロンが省略されていることに注意してください。これは重要で
す。波括弧で囲まれたブロック内で、最後のステートメントの後ろにセミコロンがない場
合、ブロック全体に最後の式の値が与えられます。

別の言い方をすると、 Rust でのセミコロンは*式の値を無視します*。よって、 `if`
のブランチが `{ 4; }` のようになっていたら、上述の例は `price` に nil (void) が
単に代入されます。しかしセミコロンがないと、それぞれのブランチが違う値を持ち、
`price` は実行されるブランチの値になります。

この特徴は関数本体でも有効です。次の関数はブール値を返します。

~~~~
fn is_four(x: int) -> bool { x == 4 }
~~~~

手短に言えば、宣言 (変数に対する `let`, 関数に対する `fn`, その他) でない全ての
ものは式です。

もしこれら全てが式だとしたら、*全ての*ステートメント、つまり C では伝統的にセミ
コロンで終端しない `while` などの後にさえ、終端のセミコロンを追加する必要がある
と結論するかもしれません。しかしこれは正しくありません。ブロックで終わる式は、
そのブロックが終端に式を含んでいるときだけ (if that block contains a trailing
expression) セミコロンが必要です。 `while` ループは終端に式を許しません。また
`if` ステートメントは、その値を使いたいときのみ終端に式を持つ傾向にあります。そ
の場合、 `if` 式は上の例での `let x = ...` のような、より大きなステートメントに
埋め込まれているでしょう。

## 識別子

Rust の識別子は C と同じ規則に従います。つまり、アルファベットかアンダースコア
から始まり、その後はアルファベット、数字、またはアンダースコアの列を含むことが
可能です。関数、変数、モジュール名は小文字で始め、可読性を助ける箇所でアンダー
スコアを用い、一方で型は大文字で始めるのが、推奨されるスタイルです。

ダブルコロン (`::`) はモジュールセパレータとして使われます。なので、
`io::println` は「 `io` という名前のモジュール内にある、 `println` という名前の
もの」を意味します。

## 変数宣言

今まで見てきたように、 `let` キーワードはローカル変数を導入します。ローカル変数
はデフォルトで immutable です。 `let mut` を用いることで、再代入できる変数を導
入できます。グローバル定数は `const` で定義できます。

~~~~
const REPEAT: int = 5;
fn main() {
    let hi = "Hi!";
    let mut count = 0;
    while count < REPEAT {
        io::println(hi);
        count += 1;
    }
}
~~~~

ローカル変数は前の宣言を隠し、前の変数をアクセス不可能にする可能性があります。

~~~~
let my_favorite_value: float = 57.8;
let my_favorite_value: int = my_favorite_value as int;
~~~~

## 型

基本型は次のように記述します。

`()`
  : Nil, 一つの値だけを持つ型。

`bool`
  : 値 `true` と `false` からなるブール型。

`int`
  : マシンポインタの大きさを持つ整数。

`uint`
  : マシンポインタの大きさを持つ符号無し整数。

`i8`, `i16`, `i32`, `i64`
  : 指定された大きさ (bit) を持つ符号付き整数。

`u8`, `u16`, `u32`, `u64`
  : 指定された大きさを持つ符号無し整数。

`float`
  : ターゲットマシンで効率的にサポートされる最大の浮動小数点数型。

`f32`, `f64`
  : 指定された大きさを持つ浮動小数点数型。

`char`
  : ユニコード文字 (32 bits) 。

これらは複合型 (詳細は後述) と組み合わせられます。ここで `T` は任意の型を表しま
す。

`[T * N]`
  : N 個の要素を持つベクタ (他の言語での配列) 。

`[mut T * N]`
  : N 個の要素を持つ変更可能なベクタ。

`(T1, T2)`
  : タプル型。 1 より大きい項数がサポートされます。

`@T`, `~T`, `&T`
  : ポインタ型。 `@`, `~`, `&` が何を意味するかの説明は
    [Boxes and pointers](#boxes-and-pointers) を見てください。

直接には扱えず、ポインタによってのみ扱える型が存在します。例えば、文字列
(`str`) を直接使うことはできず、代わりに文字列へのポインタ (`@str`, `~str`, or
`&str`) を使います。これらの*動的な大きさ*を持つ型は、次から構成されます。

`fn(arg1: T1, arg2: T2) -> T3`
  : 関数型。

`str`
  : 文字列型 (UTF-8) 。

`[T]`
  : 不明な大きさを持つベクタ (スライスとも呼ばれます) 。

`[mut T]`
  : 不明な大きさを持つ変更可能なベクタ。

型は `type` 宣言により名前を与えることが可能です。

~~~~
type MonsterSize = uint;
~~~~

これは符号無し整数型に `MonsterSize` というシノニムを提供します。 `MonsterSize`
という新しい、非互換の型を実際に作るのではありません。 `MonsterSize` と `uint`
は互いに交換可能な形で使え、一方の名前が期待される場所でもう一方の名前を使って
も型エラーを引き起こしません。単なるシノニムでない型を作る必要があるなら、
[single-variant enums](#single_variant_enum) を読んでください。

## 型の使用

`is_four` の例にある `-> bool` は、関数の戻り型を記述する方法です。意味のある値
を返さない関数については、 `-> ()` とオプショナルに記述できます。しかし、以前見
た `fn main() { ...}` の例のように、通常は戻り型の注釈を単に省略します。

関数の引数は全て `x: int` のように型を宣言する必要があります。関数内ではほとん
どのローカルなものに対し、型推論が可能です (後述する総称関数はときどき注釈が必
要です) 。ローカルなものは型注釈ありでもなしでも記述できます。

~~~~
// The type of this vector will be inferred based on its use.
let x = [];
# vec::map(x, fn&(&&_y:int) -> int { _y });
// Explicitly say this is a vector of zero integers.
let y: [int * 0] = [];
~~~~

## 数値リテラル

整数は 10 進数 (`144`) 、16 進数 (`0x90`) 、 2 進数 (`0b10010000`) と記述できま
す。サフィックスなしで (`3`, `-500`, etc.) 整数リテラルを書いたら、 Rust コンパ
イラはその型を周辺の型注釈と関数のシグニチャから推論しようとします。型注釈が全
くない場合、 Rust はサフィックスのない整数リテラルを `int` 型と仮定します。整数
リテラルをサフィックス付きで記述して、型の曖昧さを避けることも可能です。例えば、
次のようにです。

~~~~
let x = 50;
log(error, x); // x is an int
let y = 100u;
log(error, y); // y is an uint
~~~~

Rust では整数型同士の暗黙の変換が行われないことに注意してください。 `uint` 型の
変数に 1 を足すとき、 `+= 1u8` と書くと型エラーになります。

浮動小数点数は `0.0`, `1e6`, `2.1e-7` と記述します。サフィックスがない場合、リ
テラルは `float` 型であると仮定されます。サフィックス `f` (32-bit) と `l`
(64-bit) は特定の型を持つリテラルを作るのに使えます。

## 他のリテラル

nil リテラルは型と同じように `()` と記述します。キーワード `true` と `false` は
ブールリテラルを生成します。

文字リテラルは `'x'` のように、シングルクォート間に記述します。 C と同様に Rust
はバックスラッシュを使って、いくつかのキャラクタエスケープを認識します。 `\n`,
`\r`, `\t` がよく使われます。

文字列リテラルもまた同じエスケープシーケンスを許容します。それらはダブルクォー
ト間に記述されます (`"hello"`) 。 Rust の文字列は改行を含むことがあります。

## 演算子

Rust の演算子に驚くようなところはほとんどありません。二項演算子は `*`, `/`,
`%`, `+`, `-` (乗算、除算、剰余、加算、減算) で行われます。 `-` は符号を反転す
る単項演算子でもあります。 C と同様に、ビット演算子 `>>`, `<<`, `&`, `|`, `^`
もサポートされます。整数型に対して `!` を適用すると、全てのビットが反転する (C
での `~` のように) ことに注意してください。

比較演算子は伝統的な `==`, `!=`, `<`, `>`, `<=`, `>=` です。ショートサーキット
(遅延評価される) ブール演算子は `&&` (かつ) と `||` (または) と書かれます。

Rust では、型変換に `as` 演算子を使います。左側に式、右側に型を取り、意味のある
変換が存在する場合、式の結果を与えられた型に変換します。

~~~~
let x: float = 4.0;
let y: uint = x as uint;
assert y == 4u;
~~~~

C との主な違いは `++` と `--` がないことと、論理ビット演算子がより高い優先順位
を持つことです。 `x & 2 > 0` は C では `x & (2 > 0)` という結果になり、 Rust で
は `(x & 2) > 0` を意味します。これはあなたが (C の熟練者でなければ) 期待したも
のに、より近いはずです。

## 構文拡張

*構文拡張*は言語に組み込まれておらず、代わりにライブラリによって提供される特殊
形式です。構文拡張が使われていることを読み手に明確にするため、全ての構文拡張の
名前は `!` で終わります。標準ライブラリは少数の構文拡張を定義していて、最も有用
なのはコンパイル時に展開される `sprintf` スタイルのテキスト整形器 `fmt!` です。

~~~~
io::println(fmt!("%s is %d", ~"the answer", 42));
~~~~

`fmt!` は [printf][pf] がサポートするディレクティブのほとんどをサポートしますが、
ディレクティブの型が引数の型に一致しない場合、コンパイルエラーになります。

[pf]: http://en.cppreference.com/w/cpp/io/c/fprintf

このチュートリアルの範囲を超えますが、マクロシステムを使ってあなた自身の構文拡
張を定義できます。

# Control structures

## Conditionals

We've seen `if` pass by a few times already. To recap, braces are
compulsory, an optional `else` clause can be appended, and multiple
`if`/`else` constructs can be chained together:

~~~~
if false {
    io::println(~"that's odd");
} else if true {
    io::println(~"right");
} else {
    io::println(~"neither true nor false");
}
~~~~

The condition given to an `if` construct *must* be of type boolean (no
implicit conversion happens). If the arms return a value, this value
must be of the same type for every arm in which control reaches the
end of the block:

~~~~
fn signum(x: int) -> int {
    if x < 0 { -1 }
    else if x > 0 { 1 }
    else { return 0 }
}
~~~~

## Pattern matching

Rust's `match` construct is a generalized, cleaned-up version of C's
`switch` construct. You provide it with a value and a number of *arms*,
each labelled with a pattern, and the code will attempt to match each pattern
in order. For the first one that matches, the arm is executed.

~~~~
# let my_number = 1;
match my_number {
  0     => io::println("zero"),
  1 | 2 => io::println("one or two"),
  3..10 => io::println("three to ten"),
  _     => io::println("something else")
}
~~~~

There is no 'falling through' between arms, as in C—only one arm is
executed, and it doesn't have to explicitly `break` out of the
construct when it is finished.

The part to the left of the arrow `=>` is called the *pattern*. Literals are
valid patterns and will match only their own value. The pipe operator
(`|`) can be used to assign multiple patterns to a single arm. Ranges
of numeric literal patterns can be expressed with two dots, as in `M..N`. The
underscore (`_`) is a wildcard pattern that matches everything.

The patterns in an match arm are followed by a fat arrow, `=>`, then an
expression to evaluate. Each case is separated by commas. It's often
convenient to use a block expression for a case, in which case the
commas are optional.

~~~
# let my_number = 1;
match my_number {
  0 => {
    io::println("zero")
  }
  _ => {
    io::println("something else")
  }
}
~~~

`match` constructs must be *exhaustive*: they must have an arm covering every
possible case. For example, if the arm with the wildcard pattern was left off
in the above example, the typechecker would reject it.

A powerful application of pattern matching is *destructuring*, where
you use the matching to get at the contents of data types. Remember
that `(float, float)` is a tuple of two floats:

~~~~
use float::consts::pi;
fn angle(vector: (float, float)) -> float {
    match vector {
      (0f, y) if y < 0f => 1.5 * pi,
      (0f, y) => 0.5 * pi,
      (x, y) => float::atan(y / x)
    }
}
~~~~

A variable name in a pattern matches everything, *and* binds that name
to the value of the matched thing inside of the arm block. Thus, `(0f,
y)` matches any tuple whose first element is zero, and binds `y` to
the second element. `(x, y)` matches any tuple, and binds both
elements to a variable.

Any `match` arm can have a guard clause (written `if EXPR`), which is
an expression of type `bool` that determines, after the pattern is
found to match, whether the arm is taken or not. The variables bound
by the pattern are available in this guard expression.

## Let

You've already seen simple `let` bindings. `let` is also a little fancier: it
is possible to use destructuring patterns in it. For example, you can say this
to extract the fields from a tuple:

~~~~
# fn get_tuple_of_two_ints() -> (int, int) { (1, 1) }
let (a, b) = get_tuple_of_two_ints();
~~~~

This will introduce two new variables, `a` and `b`, bound to the
content of the tuple.

You may only use *irrefutable* patterns—patterns that can never fail to
match—in let bindings. Other types of patterns, such as literals, are
not allowed.

## Loops

`while` produces a loop that runs as long as its given condition
(which must have type `bool`) evaluates to true. Inside a loop, the
keyword `break` can be used to abort the loop, and `again` can be used
to abort the current iteration and continue with the next.

~~~~
let mut cake_amount = 8;
while cake_amount > 0 {
    cake_amount -= 1;
}
~~~~

`loop` is the preferred way of writing `while true`:

~~~~
let mut x = 5;
loop {
    x += x - 3;
    if x % 5 == 0 { break; }
    io::println(int::str(x));
}
~~~~

This code prints out a weird sequence of numbers and stops as soon as
it finds one that can be divided by five.

For more involved iteration, such as going over the elements of a
collection, Rust uses higher-order functions. We'll come back to those
in a moment.

# Functions

Like all other static declarations, such as `type`, functions can be
declared both at the top level and inside other functions (or modules,
which we'll come back to [later](#modules-and-crates)).

We've already seen several function definitions. They are introduced
with the `fn` keyword, the type of arguments are specified following
colons and the return type follows the arrow.

~~~~
fn repeat(string: &str, count: int) -> ~str {
    let mut result = ~"";
    for count.times {
        result += string;
    }
    return result;
}
~~~~

The `return` keyword immediately returns from the body of a function. It
is optionally followed by an expression to return. A function can
also return a value by having its top level block produce an
expression.

~~~~
# const copernicus: int = 0;
fn int_to_str(i: int) -> ~str {
    if i == copernicus {
        return ~"tube sock";
    } else {
        return ~"violin";
    }
}
~~~~

~~~~
# const copernicus: int = 0;
fn int_to_str(i: int) -> ~str {
    if i == copernicus { ~"tube sock" }
    else { ~"violin" }
}
~~~~

Functions that do not return a value are said to return nil, `()`,
and both the return type and the return value may be omitted from
the definition. The following two functions are equivalent.

~~~~
fn do_nothing_the_hard_way() -> () { return (); }

fn do_nothing_the_easy_way() { }
~~~~

# 基本データ型

Rust のコアデータ型は、 struct 、 enum (タグ付けされた共用体、代数的データ型) 、
タプルです。これらはデフォルトで変更不可能 (immutable) です。

~~~~
struct Point { x: float, y: float }

enum Shape {
    Circle(Point, float),
    Rectangle(Point, Point)
}
~~~~

## struct

Rust の struct 型は、使用する前に `struct` 構文を用いて宣言する必要があります。
`struct` 構文は `struct Name { field1: T1, field2: T2 [, ...] }` です。ここで
`T1`, `T2`, ... は型を意味します。
struct を構築するためには同じ構文を使用しますが、 `struct` を記述しません。例え
ば `Point { x: 1.0, y: 2.0 }` です。

struct は C の構造体に非常に似ていて、メモリ上に同じ方法で置かれます (従って、
Rust から C の構造体を読むことが可能で、その逆も同様です) 。 struct のフィール
ドにアクセスするには、ドット演算子を用います (`mypoint.x`) 。

mutable にしたいフィールドは明示的に `mut` と記す必要があります。

~~~~
struct Stack {
    content: ~[int],
    mut head: uint
}
~~~~

このような型では、 `mystack.head += 1u` とできます。仮に `mut` を型から省略した
場合、このような代入は型エラーになります。

## struct のパターン

struct は `match` パターンによって分解できます。基本的な構文は
`Name {fieldname: pattern, ...}` です。

~~~~
# struct Point { x: float, y: float }
# let mypoint = Point { x: 0.0, y: 0.0 };
match mypoint {
    Point { x: 0.0, y: y } => { io::println(y.to_str());                    }
    Point { x: x, y: y }   => { io::println(x.to_str() + " " + y.to_str()); }
}
~~~~

一般に struct のフィールド名は、型で現れるのと同じ順序でパターンに現れる必要は
ありません。レコードの全フィールドには興味がない場合、他のフィールドを無視する
ことを示すために、レコードパターンを `, _` で終えます (`{field1, _}` のように) 。

## enum

enum はいくつかの異なった表現を持つデータ型です。さきほど示した例を考えましょう。

~~~~
# type point = {x: float, y: float};
enum shape {
    circle(point, float),
    rectangle(point, point)
}
~~~~

この型の値は circle か rectangle のどちらか一方であり、 circle の場合は point
レコードと float 、 rectangle の場合は二つの point レコードを持ちます。このよう
な値の実行時表現には、実際に保持している形式を識別するための ID が含まれていま
す。これは C での「タグ付き共用体」に非常に似ていますが、人間工学的により良いも
のです (with better ergonomics) 。

上の宣言は、これらに対応する型 (XXX: 原文の refer to はポインタ的な意味ではない
はず。要確認)  `shape` を定義し、さらに値を構築するために使う関数 `circle` と
`rectangle` を定義します (指定された型の引数を取ります) 。よって、
`circle({x: 0f, y: 0f}, 10f)` とすると、新しい circle が作られます。

enum ヴァリアントは必ずしも型パラメタを持つ必要はありません。次の例は C の enum
と等価です。

~~~~
enum direction {
    north,
    east,
    south,
    west
}
~~~~

これは `north`, `east`, `south`, `west` を定数として定義し、その型は全て
`direction` になります。

enum が C ライクなとき、つまりパラメタを取るヴァリアントが存在しない場合、識別
子 (discriminator) の値を明示的に設定できます。

~~~~
enum color {
  red = 0xff0000,
  green = 0x00ff00,
  blue = 0x0000ff
}
~~~~

明示的な識別子がヴァリアントに指定されない場合、値は一つ前のヴァリアントの値 +
1 になります。最初のヴァリアントが識別子を持たない場合、値は 0 になります。例え
ば、 `north` の値は 0 、 `east` の値は 1 です。

enum が C ライクなら、 `as` キャスト演算子を使うことで識別子の値が得られます。

<a name="single_variant_enum"></a>

単一のヴァリアントを持つ enum の特殊なケースがあります。これは、既に存在する型
のシノニムではなく、新しく区別される型を定義するために使われます。

~~~~
enum gizmo_id = int;
~~~~

上の記述は次の省略表記です。

~~~~
enum gizmo_id { gizmo_id(int) }
~~~~

このような enum 型では、値参照 (dereference) を行う単項演算子 `*` によって内容
を取り出すことができます。

~~~~
# enum gizmo_id = int;
let my_gizmo_id = gizmo_id(10);
let id_int: int = *my_gizmo_id;
~~~~

## enum のパターン

複数のヴァリアントを持つ enum 型では、 destructuring が内容を取り出す唯一の方法
です。全てのヴァリアント構築子は、次の `area` の定義のように、パターンとして使
えます。

~~~~
# type point = {x: float, y: float};
# enum shape { circle(point, float), rectangle(point, point) }
fn area(sh: shape) -> float {
    alt sh {
        circle(_, size) { float::consts::pi * size * size }
        rectangle({x, y}, {x: x2, y: y2}) { (x2 - x) * (y2 - y) }
    }
}
~~~~

次は、パラメタのない enum をマッチングする別の例です。

~~~~
# type point = {x: float, y: float};
# enum direction { north, east, south, west }
fn point_from_direction(dir: direction) -> point {
    alt dir {
        north { {x:  0f, y:  1f} }
        east  { {x:  1f, y:  0f} }
        south { {x:  0f, y: -1f} }
        west  { {x: -1f, y:  0f} }
    }
}
~~~~

## タプル

Rust のタプルはフィールドが名前を持たない (よってドット記法ではフィールドにアク
セスできません) 点を除いて、レコードと全く同じように振舞います。タプルは 0 と 1
を除く任意の数の引数を持てます (ただし、お好みで nil, `()` を空のタプルと考える
こともできます) 。

~~~~
let mytup: (int, int, float) = (10, 20, 30.0);
alt mytup {
  (a, b, c) { log(info, a + b + (c as int)); }
}
~~~~

# Rust のメモリモデル

ここで、 Rust のメモリモデルに関わる概念について説明するため、ちょっと遠回りし
ましょう。 Rust はメモリ管理に対して非常に特徴的なアプローチを採っていて、言語
の印象を形作る上で重要な役割を果たしています。 memory landscape を理解すること
は Rust 独自の特徴に出くわしたとき、その理解を容易にしてくれるでしょう。

Rust におけるメモリの見方を特徴付ける、三つの競合する目標があります。

* メモリ安全性: Rust 言語によって管理され、アクセスできるメモリは必ず有効である
  ことが保証されます。つまり、一般的な状況下で Rust がセグメンテーションエラー
  やメモリリークを引き起こすことは不可能です。
* 性能: 高パフォーマンスで低レベルなコードでは、複数のアロケーション戦略を採用
  できる必要があります。また、低パフォーマンスで高レベルなコードには、単一のガ
  ーベッジコレクションを基本としたヒープアロケーション戦略を採用できる必要があ
  ります。
* 並列性: Rust は並列に動くコードに対しても、メモリ安全性を保証します。

## パフォーマンスの考慮がメモリモデルに与える影響

強いメモリ安全性の保証を提供するほとんどの言語は、オブジェクト全てを管理するた
めに、ガーベッジコレクションされるヒープに頼っています。これは概念的にも実装的
にも素直です。しかし著しいコストがかかります。このアプローチの採る言語は、アロ
ケーションのコストを改善する方法を積極的に追求する傾向にあります (Java 仮想マシ
ンを考えてみてください) 。 Rust はこの戦略を _ 共有ボックス (shared box)_ でサ
ポートします。これはヒープ上に割り当てられるメモリで、複数の変数から参照される
ことがあります。

対して C++ のような言語は、オブジェクトを割り当てる場所について、非常に正確な制
御が可能です。特に高価なヒープアロケーションを避けて、オブジェクトをスタック上
に直接置くことがよく行われます。 Rust でも同じことが可能で、スタックオブジェク
トが破壊された後で変数から参照されないことを保証するため、コンパイラは賢い _ポ
インタの生存期間の解析_ を使います。

## 並列性の考慮がメモリモデルに与える影響

並列環境でのメモリ安全性は、同じメモリにアクセスする 2 つのスレッド間の競合条件
を回避することに関係します。高レベル言語でさえ、多くの場合プログラムに競合条件
のないことを保証するために、プログラマが正しくロックを行うことを要求します。

Rust は、メモリがタスク間で共有できないという立場からスタートします。他言語での
経験から、各タスクのヒープを他から隔離する手法は信頼できる戦略で、プログラマに
とって理解しやすいと証明されています。ヒープの隔離は、ガーベッジコレクションが
各ヒープごとに独立して行われる、という利益もあります。 Rust はガーベッジコレク
ションのために、 "stop the world" を行うことはありません。

タスク間でヒープを完全に隔離することは、タスク間で転送されるあらゆるデータをコ
ピーする必要があることを意味します。となるように思えます。これはタスク間通信を
実装する上で十分に使える方法ですが、大きなデータ構造に対して非常に非効率です。

このため、 Rust はグローバルな _交換ヒープ (exchange heap)_ を採用します。交換
ヒープに割り当てられたオブジェクトは _ownerwhip semantics_ を持ちます。これはオ
ブジェクトを参照している変数が一つだけ存在する、というセマンティクスです。従っ
て、それらは _ユニークボックス_ として参照されます。全てのタスクはこのヒープ上
にオブジェクトを割り当て、高価なコピーを避けて他のタスクへ所有権を転送できます。

## 周知事項

Rust には、オブジェクトを割り当てられる 3 つの領域、スタック、ローカルヒープ、
交換ヒープ (exchange heap) があります。それぞれの領域に対応するポインタ型、借用
ポインタ (borrowed pointer, `&T`) 、共有ボックス (shared box, `@T`) 、ユニーク
ボックス (unique box, `~T`) があります。これら 3 つの sigil は言語を探検する上
でくり返し現れるでしょう。それぞれのポインタの適切な役割を学ぶことは、 Rust を
効率的に使う上での鍵となります。

# ボックスとポインタ

多くの現代的な言語とは対照的に、 Rust ではレコード型や enum のような複合型は、
ヒープ上に確保したメモリへのポインタとして表現され _ません_ 。それらは C や C++
と同様に、直接に表現されます。これは `let x = {x: 1f, y: 1f};` と記述したら、ス
タック上にレコードが作られることを意味します。それをデータ構造へコピーしたら、
ポインタではなくレコード全体がコピーされます。

`point` のような小さなレコードは、通常メモリを (ヒープ上に) 確保してポインタ経
由で使うより効率的です。しかし大きなレコードや変更可能なフィールドを持つレコー
ドは、ヒープ上に単一ののコピーを持ち、ポインタを通して参照する方が有用なことが
あります。

Rust は数種のポインタ型をサポートします。安全なポインタとして、ローカルヒープ上
に割り当てられる共有ボックス `@T`, 交換ヒープ上に割り当てられるユニークボックス
`~T`, 任意のメモリを指すことが可能で、寿命がコールスタックにより管理される借用
ポインタ `&T` があります。

Rust にはまた、 `*T` と記述される安全でないポインタがあります。これは安全でない
コードでのみ用いられる、全くチェックされないポインタ型です (従って典型的な Rust
のコードでは滅多に使われません) 。

全てのポインタ型は、 `*` 単項演算子で参照する値を得られます。

## 共有ボックス

共有ボックスはヒープに割り当てられ、ガーベッジコレクションされるメモリへのポイ
ンタです。共有ボックスは式に `@` 単項演算子を適用することで作られます。式の値は
ボックス化され、その結果が返されます。代入時に起こるような共有ボックスのコピー
では、ポインタのみがコピーされボックスの中身はコピーされません。

~~~~
let x: @int = @10; // New box, refcount of 1
let y = x; // Copy the pointer, increase refcount
// When x and y go out of scope, refcount goes to 0, box is freed
~~~~

共有ボックスがタスク間を横断することは絶対にありません。

> ***注意:*** 共有ボックスは現在のところ、参照カウントと cycle collection を通
> して再利用されますが、 Tracing GC に移行する予定です。

## ユニークボックス

共有ボックスとは対照的に、ユニークボックスは単一の所有者を持ち、二つのユニーク
ボックスが同じメモリを参照することはありません。全タスクの全てのユニークボック
スは、単一の _交換ヒープ_ 上に割り当てられます。そこでは所有者がユニークである
という性質から、タスク間の受け渡しが可能です。

ユニークボックスは所有者が単一なので、コピーは新しいユニークボックスの割り当て
と、内容をコピーする操作を含みます。ユニークボックスのコピーは高価なので、暗黙
にコピー操作が入る場合コンパイルエラーになります。

~~~~
let x = ~10;
let y = x; // error: copying a non-implicitly copyable type
~~~~

本当にユニークボックスをコピーしたいときは明示的に記述する必要があります。

~~~~
let x = ~10;
let y = copy x;
~~~~

ここで 'ムーブ' (`<-`) 演算子が登場します。これは `=` に似ていますが、コピー元
を de-initialize します。それゆえユニークボックスは単一の所有者を持つという制約
条件を壊すことなく `x` から `y` へ移動できます (もしムーブ演算子の代わりに代入
演算子を使ったら、原理的にはボックスはコピーされます) 。

~~~~
let x = ~10;
let y <- x;
~~~~

> ***注意:*** このコピー vs ムーブの議論は、自動的にコピー操作をムーブに置き換
> える "last use" ルールの説明ではありません。これは継続的に変更が行われる予定
> の、発展中の領域です。

ユニークボックスは共有ボックスを含まないとき、他のタスクへ送信できます。送信す
るタスクはボックスの所有権を放棄し、以後アクセスできなくなります。受信するタス
クはボックスの唯一の所有者になります。

## 借用ポインタ

Rust の借用ポインタは汎用の参照/ポインタ型で C++ の参照型に似ていますが、有効な
メモリを指していることが保証されます。ポインタ所持者が参照先メモリの所有者とな
るユニークポインタとは対照的に、借用ポインタは絶対に所有権を持ちません。ポイン
タは任意の型から借用可能で、参照先より長生きしないことが保証されます。

~~~~
# fn work_with_foo_by_pointer(f: &~str) { }
let foo = ~"foo";
work_with_foo_by_pointer(&foo);
~~~~

次の例は借用ポインタでできないことを示しています。仮にこのような記述が可能なら、
`foo` へのポインタが `foo` 自身より長生きしてしまいます。

~~~~ {.ignore}
let foo_ptr;
{
    let foo = ~"foo";
    foo_ptr = &foo;
}
~~~~

> ***注意:*** 借用ポインタは新しく言語に追加されたものです。これはまだ広範囲に
> は使われていませんが、よくある状況下、特に引数の参照渡しのために使われるよう
> になると期待されています。 Rust の現状の引数の参照渡しの解決法は [引数渡しの
> モード](#argument-passing) を参照してください。

## Mutability

全てのポインタ型は mutable な亜種を持ち、 `@mut T` または `~mut T` のように記述
します。 値参照 (dereference) 演算子と変更操作を組み合わせることで、内容を書き
換えることができます。

~~~~
fn increase_contents(pt: @mut int) {
    *pt += 1;
}
~~~~

# ベクトル

## ベクトルと文字列のメソッド

# クロージャ

今まで見てきたような名前付き関数は関数の外で宣言されたローカル変数を参照できま
せん。それが環境について閉じていないからです。例えば、次のようには記述できませ
ん。

~~~~ {.ignore}
let foo = 10;

fn bar() -> int {
   return foo; // `bar` cannot refer to `foo`
}
~~~~

Rust は _クロージャ_ もサポートしています。クロージャとは、自身を囲っているスコ
ープ内の変数にアクセスできる関数です。

~~~~
# use println = io::println;
fn call_closure_with_ten(b: fn(int)) { b(10); }

let captured_var = 20;
let closure = |arg| println(fmt!("captured_var=%d, arg=%d", captured_var, arg));

call_closure_with_ten(closure);
~~~~

クロージャはバーに挟まれた引数リストで始まり、単一の式が続きます。引数の型は戻
り型と同様、一般に省略されます。コンパイラがほとんどいつも推論可能だからです。
コンパイラが補助を必要とする稀なケースでは、引数の型と戻り型の注釈が付けられま
す。

~~~~
# type mygoodness = fn(~str) -> ~str; type what_the = int;
let bloop = |well, oh: mygoodness| -> what_the { fail oh(well) };
~~~~

数種のクロージャの形式が存在し、それぞれ固有の役割があります。一番よく使われる
_スタッククロージャ_ は `fn&` 型を持ち、囲われているスコープ内の変数に直接アク
セスできます。

~~~~
let mut max = 0;
(~[1, 2, 3]).map(|x| if x > max { max = x });
~~~~

## 共有クロージャ

(訳注: 以下原文で boxed closure と書かれている部分のいくつかを共有クロージャ
(shared closure) に変更して翻訳)

データ構造にクロージャを格納する必要があるとき、スタッククロージャを格納しよう
としてもコンパイラに拒絶されます。このため、 Rust は `fn@` と記述される、任意の
寿命を持つクロージャ型 (前述の `@` ポインタに類似の共有クロージャ) を提供します。

共有クロージャは環境に直接アクセスせず、単に値 (XXX: that it closes) をプライベ
ートなデータ構造へとコピーします。これは変数への代入が不可能で、変数の更新に「
気づく」こともないことを意味します。

次のコードは、引数に与えられた文字列を追加するクロージャを生成して関数から返し、
それを呼び出します。

~~~~
extern mod std;

fn mk_appender(suffix: ~str) -> fn@(~str) -> ~str {
    return fn@(s: ~str) -> ~str { s + suffix };
}

fn main() {
    let shout = mk_appender(~"!");
    io::println(shout(~"hey ho, let's go"));
}
~~~~

この例は長いクロージャ構文 `fn@(s: ~str) ...` を使用し、共有クロージャを宣言し
ていることを明示しています。実際には通常、共有クロージャは以前紹介した短いクロ
ージャ構文を用いて定義されます。この場合、コンパイラがクロージャの型を推論しま
す。よって、上述の例は次のようにも記述できます。

~~~~
fn mk_appender(suffix: ~str) -> fn@(~str) -> ~str {
    return |s| s + suffix;
}
~~~~

## ユニーククロージャ

`fn~` と記述され `~` ポインタ型に類似するユニーククロージャは、プロセス間で安全
に送信できるものを所有します。共有クロージャと同じように値 (XXX: that it close
over) をコピーしますが、さらにそれを「所有」します。つまり、他のコードはそれに
アクセスできません。ユニーククロージャは並列コード内で、特に[タスク][#tasks]を
生成するために使われます。

## クロージャの互換性

Rust のクロージャには、 `fn()` を期待する関数に (引数と返り値の型が合う限り) 任
意の種類のクロージャを渡せるという、素敵な性質があります。よって、引数で渡され
る関数について、単なる呼び出し以上のことをしない高階関数を書く場合は、ほぼ常に
引数の型を `fn()` と指定すべきです。そうすれば、呼び出し側が好きなものを何でも
渡せる柔軟性を持ちます。


~~~~
fn call_twice(f: fn()) { f(); f(); }
call_twice(|| { ~"I am an inferred stack closure"; } );
call_twice(fn&() { ~"I am also a stack closure"; } );
call_twice(fn@() { ~"I am a boxed closure"; });
call_twice(fn~() { ~"I am a unique closure"; });
fn bare_function() { ~"I am a plain function"; }
call_twice(bare_function);
~~~~

## do 構文

Rust のクロージャは高階関数と連携して、 `if` や `loop` のような制御構造をシミュ
レートするために頻繁に用いられます。整数のベクタをイテレーションし、それぞれの
要素にオペレータを適用する関数を考えましょう。

~~~~
fn each(v: ~[int], op: fn(int)) {
   let mut n = 0;
   while n < v.len() {
       op(v[n]);
       n += 1;
   }
}
~~~~

呼び出し側で最後のオペレータの引数を提供するためにクロージャを使うと、心地良い
ブロックのような構造を持つ方法で記述できます。

~~~~
# fn each(v: ~[int], op: fn(int)) {}
# fn do_some_work(i: int) { }
each(~[1, 2, 3], |n| {
    debug!("%i", n);
    do_some_work(n);
});
~~~~

これは役立つパターンなので、 Rust は組み込みの制御構造により近い記述が可能な、
関数呼び出しの特別な形式を用意しています。

~~~~
# fn each(v: ~[int], op: fn(int)) {}
# fn do_some_work(i: int) { }
do each(~[1, 2, 3]) |n| {
    debug!("%i", n);
    do_some_work(n);
}
~~~~

呼び出しは `do` キーワードが前に付けられ、最後のクロージャを引数リスト内に記述
する代わりに、典型的なコードブロックと視覚的により近い、括弧の外に記述します。
`do` 式は、クロージャを引数の最後にとる呼び出しの、純粋な糖衣構文です。

`do` はタスクを生成するためによく用いられます。

~~~~
use task::spawn;

do spawn() || {
    debug!("I'm a task, whatever");
}
~~~~

これは素敵ではありますが、バーと括弧に注目してください。立て続けに二つの空の引
数リストを構成しています。これらが存在しなかったら素晴らしいに違いありません。

~~~~
# use task::spawn;
do spawn {
   debug!("Kablam!");
}
~~~~

空の引数リストは `do` 式から省略できます。

## for ループ

Rust でのほとんどのイテレーションは `for` ループで行われます。 `do` のように、
`for` はクロージャでフローを制御するための素敵な構文です。加えて、 `for` ループ
内では `while` や `loop` と同じように `break`, `again`, `return` が使えます。

`each` 関数を再び考えましょう。今回は iteratee が `false` を返したら、すぐにル
ープを抜け出すように改善します。

~~~~
fn each(v: ~[int], op: fn(int) -> bool) {
   let mut n = 0;
   while n < v.len() {
       if !op(v[n]) {
           break;
       }
       n += 1;
   }
}
~~~~

そして、ベクタをイテレーションするためにこの関数を使います。

~~~~
# use each = vec::each;
# use println = io::println;
each(~[2, 4, 8, 5, 16], |n| {
    if n % 2 != 0 {
        println(~"found odd number!");
        false
    } else { true }
});
~~~~

`for` を使うことで、 `each` のような関数を組み込みのループ構造により近い形で扱
えます。 `for` ループで `each` を呼び出す場合、ループから抜け出すために `false`
を返す代わりに `break` と記述します。次のイテレーションの頭までスキップするには、
`again` と記述します。

~~~~
# use each = vec::each;
# use println = io::println;
for each(~[2, 4, 8, 5, 16]) |n| {
    if n % 2 != 0 {
        println(~"found odd number!");
        break;
    }
}
~~~~

加えて、 `for` ループの本体として現れるブロック内では、通常クロージャ内では許さ
れない `return` キーワードも使えます。これは単にループ本体から抜けるだけではな
く、外側の関数から戻ります。

~~~~
# use each = vec::each;
fn contains(v: ~[int], elt: int) -> bool {
    for each(v) |x| {
        if (x == elt) { return true; }
    }
    false
}
~~~~

`for` 構文はスタッククロージャでのみ働きます。

# Generics

## 総称関数

このチュートリアルを通して、一つのデータ型に対してのみ作用する関数を定義してき
ました。適用する型それぞれについて何度も何度も関数を定義するのは負担です。そこ
で、 Rust は関数やデータ型が型パラメタを持つことを許します。

~~~~
fn map<T, U>(vector: &[T], function: fn(T) -> U) -> ~[U] {
    let mut accumulator = ~[];
    for vector.each |element| {
        vec::push(accumulator, function(element));
    }
    return accumulator;
}
~~~~

型パラメタとともに定義されるこの関数は、 `function` の引数型とベクタの要素型が
合っている限り、任意のベクタ型に対して適用可能です。

総称関数内で、型パラメタの名前 (慣例として大文字) は不透明型 (opaque type) を表
します。その中を見ることはできませんが、周りに渡すことは可能です。

## 総称データ型

総称的な `type`, `struct`, `enum` 宣言は同じパターンに従います。

~~~~
struct Stack<T> {
    elements: ~[mut T]
}

enum Maybe<T> {
    Just(T),
    Nothing
}
~~~~

これらの宣言は `Stack<u8>` や `Maybe<int>` のような正当な型を生成します。

## kind

おそらく驚くべきことに、 'copy' (複製) 操作は全ての Rust 型に対しては定義されて
いません。リソース型 (デストラクタを持つクラス) はコピー不可能で、コピー操作が
リソースのコピーを必要とするあらゆる型 (リソースを含むレコードやユニークボック
スなど) もコピー不可能です。

このことは総称関数の取り扱いを複雑にします。もし型パラメタ `T` があるとき、その
型の値をコピーすることは可能でしょうか? Rust では、型パラメタがコピー可能な
`kind` を持つと明示的に宣言しない限り不可能です。 kind は型の型です。

~~~~ {.ignore}
// This does not compile
fn head_bad<T>(v: ~[T]) -> T { v[0] }
// This does
fn head<T: Copy>(v: ~[T]) -> T { v[0] }
~~~~

総称関数は、 kind に適合する型でのみインスタンス化可能です。つまりリソース型に
対して `head` を適当できません。 Rust には型制約 (type bound) として使える数種
の kind があります。

* `Copy` - コピー可能な型。デストラクタを持つクラスでなく、デストラクタを持つク
  ラスを含む型でもなければ、全ての型はコピー可能です。
* `Send` - 送信可能な型。共有ボックス、クロージャ (XXX: unique closure は OK じ
  ゃないの? ) 、その他ローカルヒープに割り当てられる型を含まなければ、全ての型
  は送信可能です。
* `Const` - 定数型。変更可能なフィールドや共有ボックスを含まない型です。

> ***注意:*** Rust の type kind は型制約 (type bound) として使われるとき、構文
> 的に [trait](#trait) と非常によく似ていて、便宜的に組み込みの trait と考える
> ことが可能です。実際、将来的に type kind はコンパイラが特別な知識を持つ trait
> になるでしょう。

# trait

trait は、オブジェクト指向言語がメソッドと継承を用いて解決する、値多相 (value
polymorphism) に対する Rust の答えです。例えば、複数のコレクション型に作用する
関数を書くのに用います。

> ***注意:*** この機能はとても新しく、より進んだ使い方に適用するには少し拡張が
> 必要でしょう。

## 宣言

trait はメソッドの集合で構成されます。メソッドはドット記法 `self.foo(arg1,
arg2)` を使って、値 `self` と複数の引数に対して適用できます。

例えば文字列に変換できるオブジェクトのために、trait と同じ名前のメソッド
`to_str` を一つ持つ trait `to_str` を宣言できます。

~~~~
trait to_str {
    fn to_str() -> ~str;
}
~~~~

## 実装

実際に型に trait を実装するためには、 `impl` 形式を使います。次の例は `int` と
`~str` 型に `to_str` の実装を定義します。

~~~~
# trait to_str { fn to_str() -> ~str; }
impl int: to_str {
    fn to_str() -> ~str { int::to_str(self, 10u) }
}
impl ~str: to_str {
    fn to_str() -> ~str { self }
}
~~~~

これらが与えられるとき、、 `1.to_str()` を呼び出すと `~"1"` 、また
`(~"foo").to_str()` を呼び出すと `~"foo"` が得られます。これは基本的に静的な多
重定義の一種です。 Rust は `to_str` メソッドの呼び出しを見つけると、名前の一致
するメソッドを持ち、型の一致する実装を探し出して、単純にそれを呼び出します。

## 制約付き型パラメタ

値多相の有用なところは、静的である必要がないことです。仮にオブジェクト指向言語
で、オブジェクトの sub-type が正確に判明していないとメソッドを呼び出せないとし
たら、たいしたことはできない (that would not get you very far) でしょう。
コンパイル時に型の分からないメソッドを呼びだすために、型パラメタに「制約
(bound) 」を明示できます。

~~~~
# trait to_str { fn to_str() -> ~str; }
fn comma_sep<T: to_str>(elts: ~[T]) -> ~str {
    let mut result = ~"", first = true;
    for elts.each |elt| {
        if first { first = false; }
        else { result += ~", "; }
        result += elt.to_str();
    }
    return result;
}
~~~~

この構文は型パラメタがコピー可能 (原理上は別の種類の制約) である明示する構文と
似ています。 `T` が trait `to_str` に適合すると宣言することで、関数内でその型の
値に対して trait からメソッドを呼び出すことが可能になります。また、要素の型がス
コープ内で `to_str` の実装を持たない配列に対して `comma_sep` を呼び出そうとする
と、コンパイルエラーを引き起こします。

## 多相的な trait

trait は型パラメタを含むことが可能です。一般化されたシーケンス型の trait は次の
ように記述します。

~~~~
trait seq<T> {
    fn len() -> uint;
    fn iter(fn(T));
}
impl<T> ~[T]: seq<T> {
    fn len() -> uint { vec::len(self) }
    fn iter(b: fn(T)) {
        for self.each |elt| { b(elt); }
    }
}
~~~~

実装は、 trait type を指定するために型パラメタ `T` を使う前に、 `T` を明示的に
宣言する必要があります。 Rust がこの宣言を必要とするのは、 `impl` が例えば
`seq<int>` の実装を指定することも可能だからです。 (`impl` のコロンの後ろに現れ
る) trait type は、型を定義するのではなく*参照*します。

trait によって束縛される型パラメタは、各メソッド宣言のスコープに存在します (The
type parameters bound by a trait are in scope in each of the method
declarations) 。従って、 (trait と impl のどちらかで)  `T` を `len` のための明
示的な型パラメタとして再宣言すると、コンパイルエラーになります。

## trait 内での `self` 型

trait 内では、型パラメタと見なせる特殊な型 `self` が存在します。任意の型 `T` に
対する trait の実装は `self` 型パラメタを `T` に置き換えます。次の trait は、等
値性演算をサポートする型を記述します。

~~~~
trait eq {
  fn equals(&&other: self) -> bool;
}

impl int: eq {
  fn equals(&&other: int) -> bool { other == self }
}
~~~~

型 `int` のための実装で、 `equals` が `self` 引数ではなく `int` 引数をとること
に注意してください。

## trait 型へのキャスト

上述の方法で、与えられた trait に適合する*単一の*不明な型を持つ値に対して、多相
的に振る舞う関数を定義できます。しかし、次の関数について考えてください。

~~~~
# type circle = int; type rectangle = int;
# trait drawable { fn draw(); }
# impl int: drawable { fn draw() {} }
# fn new_circle() -> int { 1 }
fn draw_all<T: drawable>(shapes: ~[T]) {
    for shapes.each |shape| { shape.draw(); }
}
# let c: circle = new_circle();
# draw_all(~[c]);
~~~~

この関数は circle の配列や square の配列 (適切な `drawable` trait が定義されて
いると仮定します) に対して呼び出せます。しかし circle と square 両方を含む配列
に対しては呼び出せません。

これが必要な場合、 trait の名前を型として使うことが可能で、関数は単純に、次のよ
うに記述することになります。

~~~~
# trait drawable { fn draw(); }
fn draw_all(shapes: ~[drawable]) {
    for shapes.each |shape| { shape.draw(); }
}
~~~~

もはや型パラメタはありません (関数を適用する単一の型がないため) 。代わりに
`drawable` 型が使われます。この型は参照カウントされるボックス型で、 `drawable`
の実装が存在する値と、メソッドを探索する場所の情報を含みます。これは多くのオブ
ジェクト指向言語での 'vtable' (仮想関数テーブル) に、非常によく似ています。

このような値を構築するためには、値を trait 型にキャストする `as` 演算子を使いま
す。

~~~~
# type circle = int; type rectangle = int;
# trait drawable { fn draw(); }
# impl int: drawable { fn draw() {} }
# fn new_circle() -> int { 1 }
# fn new_rectangle() -> int { 2 }
# fn draw_all(shapes: ~[drawable]) {}
let c: circle = new_circle();
let r: rectangle = new_rectangle();
draw_all(~[c as drawable, r as drawable]);
~~~~

これは実装についての情報と一緒に、値をボックスに格納します (実装はキャストのス
コープ内で探索されます) 。 `drawable` 型は単純にそのようなボックスを参照し、た
とえスコープ上にどんな実装があっても、ボックスに対するメソッドの呼び出しは常に
機能します。

ボックスの割り当ては、単純に型パラメタを使って値をそのまま渡すより少し高価で、
静的に解決されるメソッド呼び出しよりずっと高価です。

## trait のない実装

静的な多重定義のためだけに実装を使うつもりで、適合する trait もない場合、コロン
の後ろの型を記述しなくても構いません。ただし、これはレシーバ型と同じモジュール
で実装を定義し、レシーバ型が名前のある型 (つまり enum または class) である場合
にのみ可能です。 [single-variant enums](#single_variant_enum) が一般的な選択肢
です。
